from flask import Flask, request, render_template
from flask_cors import cross_origin
from model.main import result_fun
import os

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        file = request.files["file"]
        path = "meta.mp3"
        file.save(path)
        
        response_result = result_fun("meta.mp3")
        os.remove("meta.mp3")
        return render_template('home.html',prediction_probability="Audio chunks analysis result . {}".format(response_result), prediction_emotion = "Have a Good Day. {}".format("Kalicharan"))
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)