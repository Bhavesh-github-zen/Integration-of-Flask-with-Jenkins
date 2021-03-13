from flask import Flask, render_template,request
import subprocess

app=Flask("MyApp")

@app.route("/jenkinsjob")
def job():
    form=render_template("form.html")
    return (form)

@app.route("/jenkins", methods=["GET"])
def jenkins():
    jobname = request.args.get("jn")
    authname = request.args.get("an")
    ip = request.args.get("ip")
    user = request.args.get("u")
    password = request.args.get("p")
    u =  ("http://"+user+":"+password+"@"+ip+":8080/job/"+jobname+"/build?token="+authname)
    url = ("curl "+u)
    return subprocess.getoutput(url)
