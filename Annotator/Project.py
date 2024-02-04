import pandas as pd
import os
import gc
import random

class AnnotateProject():    
    _name = ''
    __desc = ''
    __data = pd.DataFrame()
    __text_column_name = ""
    __file_path = '%project-name%_annotate-target.csv'
    __dump_path = ""
    __id2label = []
    __label2id = {}
    __data_len = 0
    
    
    def isInitialized(self):
        return not self.__data.empty
    
    def getId2Label(self):
        if not self.isInitialized():
            return []
        return self.__id2label
    
    def __getLabel(self,id):
        return self.__id2label[id]
    
    def _save(self):        
        self.__data.to_csv(self.__file_path,index=False)
        self._saveAnnotatedOnly()
        
    def _saveAnnotatedOnly(self):
        if self.__dump_path != '':
            self.getAllAnnotated().to_csv(self.__dump_path,index=False)

    def initialize(self,config):
        self._name = config['Name']
        self.__desc = config['Description']
        self.__id2label = config['Target-Annotations']
        self.__label2id = {label:id for id, label in enumerate(self.__id2label)}

        self.__text_column_name = config['Source-Text-Label']
        self.__file_path = self.__file_path.replace("%project-name%",self._name.lower().strip())
        
        self.__dump_path = config['Data-Destination-Path'].strip()
        ##-----------------------------
        ##------------------------------
        if os.path.exists(self.__file_path):
            self.__data = pd.read_csv(self.__file_path)

            if 'label' not in self.__data:
                self.__data['label'] = None

            if 'label_id' not in self.__data:
                self.__data['label_id'] = None

            self.__data['label'] = self.__data['label'].fillna(' ')
            self.__data['label_id'] = self.__data['label_id'].fillna(-1)            
        
            ## make a local copy of the source file 
            self._save()
            self.__data = pd.read_csv(self.__file_path)
            gc.collect()
        else:   
            self.__data = pd.read_csv(config['Data-Source-Path'])
        
        self.__data.index = range(self.__data.shape[0])
        self.__data_len = self.__data.shape[0]
        
    
    def selectRandomRow(self):  
        data = self.getAllNotAnnotated()
        if not data.empty:
            index = random.choice(data.index)
            return {"data":data.loc[index].to_dict(),'index':int(index),'remaining':int(data.shape[0]),'total':int(self.__data_len),'txt-col-name': self.__text_column_name}
        else:
            return pd.DataFrame.from_dict({})
        
    def setLabel(self,index,label):        
        index = int(index)
        label = int(label)
        # print(self.__id2label)
        self.__data.at[index,'label_id'] = label
        self.__data.at[index,'label'] = self.__getLabel(label)
        self._save()
        return self.__data.loc[index]
    
    def getAllAnnotated(self):
        return self.__data[self.__data['label_id'] != -1]
    
    def getAllNotAnnotated(self):
        return self.__data[self.__data['label_id'] == -1]