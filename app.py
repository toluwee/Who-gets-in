import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# create Flask instance
app = Flask(__name__)

# Load pickle
model = pickle.load(open("model.pkl","rb"))

# Create home page to render index.html
@app.route('/')
def home():
    """
    To render home page
    """
    return render_template('index.html')

# create the web API to display prediction result
@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results in HTML GUI
    """
    # collect all input feature values into a list
    int_features = [float(x) for x in request.form.values()]
    # convert list to array
    # final_features = [np.array(int_features)]
    final_features = [np.array(int_features)]
    # predict the target value from input
    prediction = model.predict(final_features)

    # get the prediction in two decimal places
    output = round(prediction[0], 2)

    # What is displayed
    return render_template('index.html', prediction_text="Probability of getting graduate school admission is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)

