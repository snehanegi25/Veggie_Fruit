# app.py

import pickle
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open('LRModel.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

# app.py

# ... (other imports and code) ...

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        commodity = request.form['commodity']
        year = int(request.form['year'])
        average = int(request.form['average'])
        unit = request.form['unit']

        # Create a DataFrame for prediction
        prediction_data = pd.DataFrame({
            'Commodity': [commodity],
            'Year': [year],
            'Average': [average],
            'Unit': [unit]
        })

        # Make a prediction using the model
        prediction = model.predict(prediction_data)

        return render_template('result.html', prediction=prediction[0])

# ... (the rest of your code) ...

if __name__ == '__main__':
    app.run(debug=True)


