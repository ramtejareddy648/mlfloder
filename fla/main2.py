from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return "about us"

@app.route('/form',methods=['GET',"POST"])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f' hello {name}!'
    return render_template('from.html')

# @app.route('/submit1',methods=["GET",'POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'{name}!'
#     return render_template('from.html')


if __name__=="__main__":
    app.run(debug=True)