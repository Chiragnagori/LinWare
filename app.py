from flask import Flask, app ,render_template , request,flash
from pymongo import MongoClient
import flask

app=Flask("nsp")
@app.route ("/")
def signup():
    return render_template("index.html")

@app.route ("/web" ,methods=["GET"])
def login():

    elog=request.args.get("emaillog")
    print(elog)
    passwdlog=request.args.get("passlog")
    print(passwdlog)
    client=MongoClient("mongodb://127.0.0.1:27017/")
    db=client["webdb"]
    Credentials=db["webdb"]
    check=db.Credentials.count({"emails":elog,"password":passwdlog})
    print(check)

    if check==1:
      return render_template("hindex.html")
    else:
      return "invalid Credential"

@app.route ("/web1", methods=["GET"])
def web():
    x1=request.args.get("name")
    x2=request.args.get("email")
    x3=request.args.get("password")
    
    client=MongoClient("mongodb://127.0.0.1:27017/")
    print(client)

    db=client["webdb"]
    print(db)
    Credentials=db["webdb"]

    records={"name": x1,"emails": x2,"password": x3 ,}
    print(records)

    db.Credentials.insert_one(records)
    final=client["db"]["Credentials"].find()
    print(final)

    return render_template("hindex.html")
    

@app.route ("/forgot")
def forgot(): 
    return render_template("forget.html")
@app.route ("/final",methods=["GET"])
def finalsite():
    upemail=request.args.get("newemail")
    uppass=request.args.get("newpass")
    print(uppass)
    print(upemail)
    client=MongoClient("mongodb://127.0.0.1:27017/")
    print(client)

    db=client["webdb"]
    print(db)
    Credentials =db["webdb"]
    a=db.Credentials.update({"emails": upemail },{"$set":{"password":uppass}})
    print(a)
    return render_template("index.html")

@app.route ("/selector")
def selector():
    return render_template("hindex.html")
    
@app.route ("/image" ,methods=["GET"] )
def image():
    ximage=request.args.get("imagename")
    if ximage=="redhat":
        return render_template("redhat.html")
    elif ximage=="centos":
        return render_template("centos.html")
    else:
        return render_template("ubuntu.html")

@app.route ("/navi_home" ,methods=["GET"] )
def navhome():
    return render_template("hindex.html")

@app.route ("/navi_aboutus" ,methods=["GET"] )
def navaboutus():
    return render_template("about.html")

@app.route ("/navi_team" ,methods=["GET"] )
def navteam():
    return render_template("getintouch.html")    
app.run(host="192.168.99.1" , port=8080)
