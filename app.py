from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join("model", "model (2).h5")
model = tf.keras.models.load_model("C:\\Users\\Ashifa\\OneDrive\\Desktop\\pneumoniadetection\\backend\\model (2).h5")

def preprocess_image(image):
    image = image.resize((150, 150))  # Resize to match model input size
    image = np.array(image) / 255.0   # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read()))
    image = preprocess_image(image)

    # Predict
    prediction = model.predict(image)
    result = "Pneumonia" if prediction[0][0] > 0.5 else "Normal"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
