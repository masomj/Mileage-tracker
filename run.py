from flask import Flask, render_template, request, flash
import os
import json
app = Flask(__name__)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True #allows arbritaray code to be run - security flaw, only for testing mode = false for submissions
    )

@app.route("/")
def index():
    return render_template("index.html")


print("hello")
