from flask import Flask, request, jsonify, send_from_directory
from model import predict_weather

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = [
        float(data.get('minTemp')),
        float(data.get('maxTemp')),
        float(data.get('Rainfall')),
        float(data.get('Evaporation')),
        float(data.get('Sunshine')),
        float(data.get('WindGustSpeed')),
        float(data.get('Humidity')),
        float(data.get('Pressure')),
        float(data.get('Cloud')),
        float(data.get('Temp9am')),
        float(data.get('Temp3pm')),
        float(data.get('Rain')),
        float(data.get('Risk_MM'))
    ]
    prediction = predict_weather(input_data)
    result = "It will rain tomorrow" if prediction == 1 else "No rain tomorrow"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
