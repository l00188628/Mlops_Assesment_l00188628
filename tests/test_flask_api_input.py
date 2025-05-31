from flask import Flask, request, jsonify
import joblib
import socket

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Check if 'age' is provided
    age = data.get('age')
    if age is None:
        return jsonify({'error': 'Missing "age" in request'}), 400

    # Validate age is a number
    try:
        age = float(age)
    except (TypeError, ValueError):
        return jsonify({'error': '"age" must be a numeric value'}), 400

    # Make prediction
    try:
        prediction = model.predict([[age]])[0]
    except Exception as e:
        return jsonify({'error': f'Model prediction failed: {str(e)}'}), 500

    return jsonify({
        'predicted_salary': prediction,
        'served_by': socket.gethostname()
    })
