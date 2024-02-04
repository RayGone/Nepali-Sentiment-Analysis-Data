from flask import Flask, render_template, redirect, url_for, request, jsonify

import json
import pandas as pd
import random
import Project

random.seed(999)

app = Flask("Annotator",
            static_url_path='', 
            static_folder='static')

app.config.from_pyfile('.env')
app.config['PROJECTS'] = json.load(open(app.config['PROJECT_CONFIG'],'r'))['Projects']

project = Project.AnnotateProject()

@app.route('/',methods=['GET'])
def index():   
    projects = app.config['PROJECTS'] 
    return render_template('index.html', name='index', projects=projects, num_of_projects = len(projects))

@app.route("/init-project",methods=['GET'])
def initialize():
    name = request.args.get('project-name')
    for config in app.config['PROJECTS']:
        if config['Name'] == name:
            project.initialize(config)
            break
        
    return redirect(url_for('annotate'))
    
@app.route('/Annotate',methods=['GET'])
def annotate():
    if not project.isInitialized():
        return redirect(url_for('index'))
    
    return render_template('annotationUI.html',name=project._name, labels = project.getId2Label())

@app.route("/get_next_item",methods=['GET'])
def getItem():
    row = project.selectRandomRow()
    if not pd.DataFrame.from_dict(row).empty:
        return row
    else:
        return {'error':'No more'}


@app.route("/set_label",methods=['POST'])
def setItem():
    # index = request.form.get('index')
    # label = request.values.get('label')
    index = request.json['index']
    label = request.json['label']
    data = project.setLabel(index,label)
    return jsonify(data.to_dict())


if __name__ == '__main__':    
    print(app.url_map)
    app.run()
    pass