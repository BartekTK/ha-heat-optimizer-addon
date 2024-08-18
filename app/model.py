from flask import Flask, request, jsonify
import joblib

# Load your trained model
model = joblib.load('heat_optimization_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [
        data['solar_forecast'],
        data['battery_soc'],
        data['inverter_power'],
        data['current_temp']
    ]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
