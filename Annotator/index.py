from flask import Flask
from flask import render_template
import pandas as pd
import random

random.seed(999)

__id2label = {
    0 : "NEUTRAL",
    1 : "POSITIVE",
    2 : "NEGATIVE"
}

file_path = 'annotate-target.csv'

##-----------------------------
app = Flask("Annotator",
            static_url_path='', 
            static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True
##------------------------------

data = pd.read_csv(file_path)
data.index = range(data.shape[0])
print(data.shape)

if 'label' not in data:
    data['label'] = None

if 'label_id' not in data:
    data['label_id'] = None

data['label'] = data['label'].fillna('')
data['label_id'] = data['label_id'].fillna(-1)

@app.route('/')
def index():    
    return render_template('index.html', name='index')

@app.route("/get_next_item")
def getItem():
    unlabeled = data[data['label_id'] == -1]
    if not unlabeled.empty:
        index = random.choice(unlabeled.index)
        return {"data":dict(data.loc[index]),'index':int(index),'remaining':int(unlabeled.shape[0])}
    else:
        return {'error':'No more'}


@app.route("/set_label/<index>/<label>")
def setItem(index,label):
    
    index = int(index)
    label = int(label)
    data.at[index,'label_id'] = label
    data.at[index,'label'] = __id2label[label]
    data.to_csv(file_path,index=False)
    return dict(data.loc[index])


if __name__ == '__main__':
    app.run()