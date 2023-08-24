from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Initialize CORS with your Flask app

model = None

def load_model():
    global model
    with open('heartDiseaseMlUpdated.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        load_model()

    request_data = request.json
    
    # Extract features from request data
    age = request_data.get('age')
    sex = request_data.get('sex')
    cp = request_data.get('cp')
    trestbps = request_data.get('trestbps')
    chol = request_data.get('chol')
    fbs = request_data.get('fbs')
    restecg = request_data.get('restecg')
    thalach = request_data.get('thalach')
   
    
    slope = request_data.get('slope')
    ca = request_data.get('ca')
    thal = request_data.get('thal')

    # Make the prediction using the model
    prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,slope, ca, thal]])

    # Return the prediction as a JSON response
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
