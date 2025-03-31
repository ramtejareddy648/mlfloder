from flask import Flask,request
from flask import render_template


app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>this is index this content write use html tags</h1>"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/about",methods=["GET","POST"])
def about():
    if request.method=="POST":
        name=request.form["name"]
        return f"your  is {name}"
    return render_template("from.html")

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('from.html')

if __name__=="__main__":
    app.run(debug=True)