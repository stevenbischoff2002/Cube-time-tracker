from pydoc import cli
import scrambleGenerator
import db_handler
import json
from flask import Flask, render_template, redirect, url_for, abort, request

global db

app = Flask(__name__)

@app.errorhandler(405)
def method_not_allowed(error):
    return redirect("/")

@app.route("/")
def index():
    return render_template("index.html",db=db.db)

@app.route("/add",methods=["POST"])
def add():
    if request.method == "POST":
        # print(json.load(request.form["scramble"]))
        time = str(request.form.get("time"))
        # scramble = str(request.form.get("scramble"))
        return(time)
    else:
        abort(418)

def cliMain(db):
    run = True
    while run:
        try:
            scramble = scrambleGenerator.gen_scramble()
            print(f"\n{scramble}\n")
            time = input("Time (**:**.***) ---> ")
            if(time.lower() in ["stop","exit","quit"]):
                print("Exiting")
                break
            min = 60 * 1000 * int(time.split(":")[0])
            sec = 1000 * int(time.split(":")[1].split(".")[0])
            msec = int(time.split(":")[1].split(".")[1])
            db.addEntry(scramble,(min + sec + msec))
        except ValueError:
            print("invalid value")



if(__name__ == "__main__"):
    mode = str(input("[CLI/web] (CLI) ---> ")).lower()
    if (mode == "cli" or len(mode) == 0):
        mode = "cli"
        print("cli")
    elif (mode == "web"):
        print("web")
    else:
        print("invalid")
        exit()
    dbFile = str(input("db Path ---> "))
    db = db_handler.DB(dbFile)
    if (mode == "cli"):
        cliMain(db)
    elif (mode == "web"):
        app.run("0.0.0.0", port=5000, threaded=True, debug=True)
