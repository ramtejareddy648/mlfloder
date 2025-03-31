from flask import Flask


app=Flask(__name__)

@app.route("/")
def home():
    return "this is home page"

@app.route("/index")
def index():
    return "<h1>this is index this content write use html tags</h1>"



if __name__=="__main__":
    app.run(debug=True)