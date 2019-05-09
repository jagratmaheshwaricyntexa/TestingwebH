from flask import Flask,request
import json
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/gitHook",methods = ['GET', 'POST'])
def salvador():
    reqData = request.form
    reqJSON = reqData.to_dict()
    print(reqData)
    print(reqJSON)
    jdata = json.loads(reqData['payload'])
    print(jdata['ref'])
    return "Hello, GitHook"
    print ("Converting SFDX to Metadata")

    datapull=os.system('git pull origin master')
    print ("####Data Pull Completed####")
    if(datapull==0):
        os.system('sfdx force:source:convert -d mdapioutput/')
        deployData=os.system('ant deployUnpackaged')
        if(deployData==0):
            print ("Deployment success")
        else:
            print ("Deployment Failed")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")