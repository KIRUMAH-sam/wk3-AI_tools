# App for MNIST Digit Classification
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

st.title("🧠 Handwritten Digit Classifier (MNIST)")
st.write("Upload an image of a digit (0–9) and let the AI predict!")

uploaded_file = st.file_uploader("Upload Image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')
    image = ImageOps.invert(image)
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    model = tf.keras.models.load_model("mnist_model.h5")
    prediction = model.predict(img_array)
    st.image(image, caption=f"Prediction: {np.argmax(prediction)}", width=150)
    st.success(f"Predicted Digit: {np.argmax(prediction)} ✅")

