from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "this is home page"

@app.route("/index")
def index():
    return "<h1>this is index this content write use html tags</h1>"


@app.route("/about")
def about():
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)