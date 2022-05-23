from flask import Flask, render_template, request, flash
import os 
import json
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cv20", methods=["GET","POST"])
def cv20():    
    
    start_location = request.form.get("start-location")
    end_location = request.form.get("end-location")
    start_mileage = request.form.get("start-mileage")
    end_mileage = request.form.get("end-mileage")
    username = request.form.get("username")
    start_time = request.form.get("start-time")
    end_time = request.form.get("end_time")
    print(end_time)
    print(start_time)
    return render_template("cv20.html")
        

@app.route("/cu18", methods=["GET","POST"])
def cu18():
    return render_template("cu18.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True #allows arbritaray code to be run - security flaw, only for testing mode = false for submissions
    )