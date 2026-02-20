from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]

        prediction = model.predict(final_features)

        if prediction[0] == 1:
            result = "⚠️ DDoS Attack Detected!"
        else:
            result = "✅ Normal Traffic"

        return render_template("index.html", prediction_text=result)

    except:
        return render_template("index.html", prediction_text="Error in Input Values")

if __name__ == "__main__":
    app.run(debug=True)