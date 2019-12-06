# Robert Lynch
# (C) 2019
#
# Marist College MSIS 621 - Fall 2019
#
from flask import Flask, render_template, request
from data import IBMcloudFunctions, IBMcloudPost


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/getdata')
def getData():
    return render_template("getdata.html", switches=IBMcloudFunctions()['entries'])

@app.route('/getDataForSwitchWithID/<string:id>/')
def getDataForSwitchWithID(id):
    #switches=Switches
    switches=IBMcloudFunctions()['entries']
    for objects in range(len(switches)):
        if switches[objects]['slug']==id:
            index=objects
            break
    return render_template("getDataForSwitchWithID.html", id=id, switches=switches[index], switchesList=switches)
@app.route('/adddata', methods=["POST", "GET"])
def addData():
    if request.method=="POST":
        if request.form["name"]!='' and request.form["slug"]!='' and request.form["firmware"]!='':
            name=request.form["name"]
            slug=request.form["slug"]
            firmware=request.form["firmware"]
            putData={
                'name':name,
                'slug':slug,
                'recommendedVersion':firmware
            }
            if IBMcloudPost(putData)["ok"]==True:
                return render_template("addDataSuccess.html")
            else:
                return render_template("addDataFailed.html")
        else:
            return render_template("addDataFailed_values.html")

    else:
        return render_template("addData.html")



if __name__=="__main__":
    app.run(host="0.0.0.0")
