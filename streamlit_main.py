import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load your trained Keras ANN model
model = load_model("model.h5")

# Streamlit UI
st.title("💳 Fraud Detection System")
st.write("Enter the 29 input values separated by commas (e.g., 0.1, -1.3, ..., 0.5)")

# Input area
user_input = st.text_area(" Input for 29 Features:", placeholder="Enter 29 comma-separated values here...")

# Predict button
if st.button(" Predict"):
    try:
        # Process input
        input_list = list(map(float, user_input.strip().split(",")))
        
        if len(input_list) != 29:
            st.error("You must enter exactly 29 values.")
        else:
            # Convert to proper shape
            input_array = np.array(input_list).reshape(1, -1)
            
            # Make prediction
            prediction = model.predict(input_array)
            fraud_prob = prediction[0][0]

            # Show result
            st.write(f"Model Confidence: `{fraud_prob:.4f}`")
            if fraud_prob >= 0.4:  # You can tweak this threshold
                st.success("The transaction is **FRAUDULENT**.")
            else:
                st.success("The transaction is **LEGITIMATE**.")
    except Exception as e:
        st.error(f" Error: {str(e)}. Please ensure input is 29 valid numbers separated by commas.")
