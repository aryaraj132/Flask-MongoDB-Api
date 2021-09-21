from flask import Flask, request
import pymongo, json
from bson import json_util
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://aryaraj132:947121@cluster0.9mn0b.mongodb.net/DB01?retryWrites=true&w=majority")
db = client.DB01


@app.route('/get-data', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json() # Your form's
        token_count = db.Token.count_documents({'token':data['token']})
        if token_count == 1:
            data = db.Col01.find({},{'_id':0})[0]
            data.update({'img':'https://webassets.mongodb.com/_com_assets/cms/mongodb_atlas_header-o7ki9pj40p.png'})
            return json.loads(json_util.dumps(data))
        else:
            data = db.Col01.find({},{'_id':0,'Email':0,'Phone':0,'Address':0})[0]
            data.update({'img':'https://webassets.mongodb.com/_com_assets/cms/mongodb_atlas_header-o7ki9pj40p.png'})
            return json.loads(json_util.dumps(data))
    else:
        data = db.Col01.find({},{'_id':0,'Email':0,'Phone':0,'Address':0})[0]
        data.update({'img':'https://webassets.mongodb.com/_com_assets/cms/mongodb_atlas_header-o7ki9pj40p.png'})
        return json.loads(json_util.dumps(data))

if __name__=="__main__":
    app.run(threaded=True)