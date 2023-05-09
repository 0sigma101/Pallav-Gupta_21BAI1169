from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load(r'C:\Users\Admin\Desktop\MIC\Pallav-Gupta_21BAI1169\WebSide\Server\Artifact\home_prices_model.pickle')

@app.route('/')
def index():
    return 'Hello'

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()
    
    #preprocessing data left
    
    prediction = model.predict(data)

    response = jsonify({
        'estimated_price': prediction
    })

    return response

if __name__ == "__main__":
    app.run(debug=True)