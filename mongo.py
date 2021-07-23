from flask import Flask, jsonify,request, Response
import json
from urllib.request import urlopen
import pymongo 
from bson import ObjectId

app = Flask(__name__)



client = pymongo.MongoClient('mongo.servers.nferx.com',username='naveen.k',password='h5aqquk3xr2vvv6')
my_db = client["naveen"]
y1 = my_db["dataset"]  
y2 = my_db["models"]  

@app.route('/')
def index():
    return ("Use /project? to add dateset and models")




@app.route('/project',methods=["GET"])
def project():
    project_id = request.args.get('id')
    given_url = "http://sentenceapi2.servers.nferx.com:8015/tagrecorder/v3/projects/" + project_id
    response = urlopen(given_url)
    data_json = json.loads(response.read())
    y1.insert_many(data_json['result']['project']['associated_datasets'])
    y2.insert_many(data_json['result']['project']['models'])
    return("Successfully uploaded to mongo")

if __name__=="__main__":
    app.run( host='0.0.0.0', port=81, debug=True)    
