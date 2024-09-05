import streamlit as st
import cv2
import tempfile
from utils import process_frame

def run():
    st.title("Video Upload Mode: PPE Detection in Pre-Recorded Videos")
    st.divider()
    st.write("""
        In this mode, you can upload a pre-recorded video to analyze whether workers are following safety protocols.
        
        **Instructions:**
        1. Click on the "Browse files" button below to upload a video file.
        2. The video formats supported include MP4, MOV, AVI, and MKV.
        3. Once uploaded, the system will process each frame to detect helmets and vests.
        4. The processed video will be displayed, highlighting any safety violations.
    """)

    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi", "mkv"])
    
    if uploaded_video is not None:
        # Save the uploaded video to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video_file:
            temp_video_file.write(uploaded_video.read())
            temp_video_path = temp_video_file.name
        
        # Load video using OpenCV
        cap = cv2.VideoCapture(temp_video_path)
        stframe = st.empty()

        while True:
            success, img = cap.read()
            if not success:
                st.write("Failed to capture image")
                break

            # Process the frame
            img = process_frame(img, confidence_threshold=50)

            # Display the frame in Streamlit
            stframe.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")

            # Break loop on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
