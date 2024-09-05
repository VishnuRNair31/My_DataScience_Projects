import streamlit as st
import cv2
import numpy as np
from utils import process_frame

def run():
    st.title("Image Upload Mode: PPE Detection in Images")
    st.divider()
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    st.write("""
        In this mode, you can upload an image to check if workers are following safety protocols.
        
        **Instructions:**
        1. Click on the "Browse files" button below to upload an image file.
        2. The image formats supported include JPG, JPEG, and PNG.
        3. Once uploaded, the system will process the image to detect Person, helmets, and vests.
        4. The processed image will be displayed with bounding boxes highlighting any safety violations.
    """)
    if uploaded_image is not None:
        # Display image processing layout
        col1, col2 = st.columns(2)

        # Add slider to adjust confidence threshold
        confidence_threshold = st.slider("Confidence Threshold", min_value=0, max_value=100, value=50)

        org_img = uploaded_image
        file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        # Process the image with the selected confidence threshold
        processed_img = process_frame(img, confidence_threshold)

        # Display original and processed images side by side
        col1.image(org_img, caption="Original Image")
        col2.image(cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB), caption="Detection Image")
