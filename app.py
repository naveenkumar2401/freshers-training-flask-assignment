from flask import Flask, jsonify,request, Response
import pymongo
import json
from urllib.request import urlopen
from bson import ObjectId

app = Flask(__name__)

client = pymongo.MongoClient('mongo.servers.nferx.com',username='naveen.k',password='h5aqquk3xr2vvv6')
mydb = client["naveen"]
y1 = mydb["dataset"]  
y2 = mydb["models"]  

@app.route('/')
def index():
    return ("Use endpoint name along with id:-  /project?id or /model?id or /dataset?id")  #main endpoint





@app.route('/project',methods=["GET"]) #project endpoint
def project():
    project_id = request.args.get('id')  
    given_url = "http://sentenceapi2.servers.nferx.com:8015/tagrecorder/v3/projects/" + project_id
    response = urlopen(given_url)
    data_json = json.loads(response.read())
    return(jsonify(data_json))

@app.route('/dataset',methods=["GET"])  #dataset endpoint
def dataset():
    dataset_id = request.args.get('id')
    myquery = {"_id": dataset_id}
    mydoc = y1.find(myquery)
    list_cur = list(mydoc)
    jss=json.dumps(list_cur)
    js=json.loads(jss)
    return (jsonify(js))

@app.route('/models',methods=["GET"]) #models endpoint
def model():
    model_id = request.args.get('id')
    putquery = {'_id':ObjectId(model_id)}
    mydoc = y2.find(putquery)
    list_ = list(mydoc)
    jss=json.dumps(list_ , default=str)
    js=json.loads(jss)
    return(jsonify(js))

if __name__=="__main__":
    app.run(debug=True) #marking true and keeping it for development purposes only