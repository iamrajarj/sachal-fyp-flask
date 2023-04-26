from flask import Flask, request, render_template, redirect, url_for, Response, jsonify
import requests
import pickle
import logs
import cv2

app = Flask(__name__)
# set Log
app.logger.addHandler(logs.file_handler)
app.logger.setLevel(logs.logging.DEBUG)
# set Log
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return redirect(url_for('index'))

@app.route("/<name>")
def check(name):
    # return f"hello {name}"
    return redirect(url_for('about'))

@app.route("/about")
def about():
    var1 = "Sachal"
    return render_template('about.html',varval = var1)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/our-work")
def ourwork():
    return render_template('ourwork.html')

@app.route("/predict")
def predict():
    return render_template('predict.html')

@app.route("/predict", methods=['POST', 'GET'])
def predicts():
    city_name = float(request.form['Enter City Name: '])

    # result = model.predict([city_name])
    result = 213
    return render_template('predict.html', **locals())

@app.route('/predictapi', methods=['POST'])
def predictapi():
    try:
        app.logger.info("apicall")
        # # Send a POST request to the Flask API with the image file as data
        response = requests.post("http://192.168.100.8:5000/predict", json={'file':"here"})
        prediction = response.json()
        app.logger.info(prediction)
        
        return jsonify(prediction),200
            
    except Exception as e:
        app.logger.error(str(e))
        msg = str(e)
        return jsonify({'message':msg})
    


if __name__ =='__main__':
    app.run(debug=True)