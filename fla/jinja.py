from flask import Flask
from flask import render_template
from flask import request,redirect,url_for

app=Flask("__name__")

@app.route("/")
def home():
    return "<h1>this is home page</h1>"

@app.route("/sucess/<int:score>")
def sucess(score):
    res=""
    if score>=50:
        res="passed"
    else:
        res="failed"
    return render_template("result.html",results=res)


@app.route("/sucessfor/<int:score>")
def sucessfor(score):
    res=""
    if(score>=50):
        res="pass"
    else:
        res="fail"
    res1={"score":score,"res":res}
    return render_template("result1.html",results=res1)
        
@app.route("/sucessif/<int:score>")
def sucessif(score):
    return render_template("result2.html",results=score)


@app.route("/submit",methods=["GET","POST"])
def re():
    if request.method=="POST":
        science1=float(request.form["science"])
        social1=float(request.form["social"])
        c1=float(request.form["c"])
        python1=float(request.form["python"])
        res=(science1+social1+c1+python1)/4
    else:
        return render_template("marks.html")
    return redirect(url_for("sucessfor",results1=res))





if __name__=="__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
