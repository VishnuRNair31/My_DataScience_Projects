import streamlit as st
import cv2
from utils import process_frame

def run():
    st.title("Webcam Mode: Real-Time PPE Detection")
    st.divider()
    st.write("""
        This mode allows you to monitor workers in real-time through the camera. The system detects whether the workers 
        are wearing the required safety gear such as helmets and vests. If a worker is found without the necessary equipment, 
        the system will automatically issue a warning.
    """)

    # Start webcam
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while True:
        success, img = cap.read()
        if not success:
            st.write("Failed to capture image")
            break

        # Process the frame
        img = process_frame(img, confidence_threshold=40)

        # Display the frame in Streamlit
        stframe.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")

        # Break loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
