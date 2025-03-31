from flask import Flask,Response,render_template,url_for
import cv2


app=Flask(__name__)

camera=cv2.VideoCapture(0)

def generate_frame():
    while True:
        sucess,frame=camera.read()
        if not sucess:
            break
        else:
            res,buffer=cv2.imencode(".jpg",frame)
            frame=buffer.tobytes()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/video")
def video():
    return Response(generate_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__=="__main__":
    app.run(debug=True)