from flask import Flask
from flask import jsonify
from waitress import serve
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app=app,host=dataConfig["url-backend"],port=dataConfig["port"])
