from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Github Pages

location = "Unknown"

# API route
@app.route('/api/meteo/', methods=['GET'])
def getMeteoAPI_info():

    # get location from gemini
    global location
    location = "Gemini Location"

    #meteo api get info 
       

    return jsonify({'result': apiInfo, 'perceptron': 'perceptron_output'})


@app.route('/api/location/', methods=['GET'])
def getLocation():
    return jsonify({'location': location})


@app.route('/api/perceptronGuess/', methods=['GET'])
def getPerceptronPrediction():

    perceptronGuess = "Perceptron Prediction"

    return jsonify({'perceptronPrediction': perceptronGuess})


if __name__ == '__main__':
    app.run(debug=True)
