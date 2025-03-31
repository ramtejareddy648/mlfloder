from flask import Flask

app=Flask(__name__)


@app.route('/')
def home():
    return "this is home page"

@app.route("/in")
def index():
    return "this is index page"


@app.route('/about')
def about():
    return "about us "
    


if __name__=="__main__":
    app.run(debug=True)
    
