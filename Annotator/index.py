from flask import Flask
from flask import render_template
import pandas as pd
import random

__id2label = {
    0 : "NEUTRAL",
    1 : "POSITIVE",
    2 : "NEGATIVE"
}

file_path = 'annotated.csv'

##-----------------------------
app = Flask("Annotator")
app.config['TEMPLATES_AUTO_RELOAD'] = True
##------------------------------

data = pd.read_csv(file_path)
data.index = range(data.shape[0])

if 'label' not in data:
    data['label'] = None

if 'label_id' not in data:
    data['label_id'] = None


@app.route('/')
def index():    
    return render_template('index.html', name='index')

@app.route("/get_next_item")
def getItem():
    if not data[~data['label_id'].isna()].empty:
        index = random.choice(data[~data['label_id'].isna()].index)
        print(index)
        return {"data":dict(data.loc[index]),'index':index}
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