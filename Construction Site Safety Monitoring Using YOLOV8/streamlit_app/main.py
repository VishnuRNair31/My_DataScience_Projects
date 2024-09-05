import streamlit as st
from streamlit_option_menu import option_menu

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://github.com/VishnuRNair31/movie/blob/main/City_Landscape_Background.jpg?raw=true");
        background-size: cover;
        background-position: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    mode = option_menu("Select Mode", ["Home", "Webcam", "Video Upload", "Image Upload","Performance Metrics"],
                       icons=["house", "camera-video", "upload", "image","bar-chart"], menu_icon="cast", default_index=0,
                       orientation="vertical")

if mode == "Home":
    st.write("# *Construction Site Safety Monitoring*")
    st.divider()
    st.write("""
        This application is designed to enhance safety at construction sites by monitoring workers for proper safety gear usage.
        """)
    st.write("""
            **Features:**
        - Real-time detection of helmets and vests using a webcam.
        - Process and analyze pre-recorded videos for safety compliance.
        - Image upload option to verify safety gear in still images.
        - Automatic warning alerts when workers are not wearing the required safety gear.
    """)

elif mode == "Webcam":
    import webcam
    webcam.run()

elif mode == "Video Upload":
    import video_upload
    video_upload.run()

elif mode == "Image Upload":
    import image_upload
    image_upload.run()

elif mode == "Performance Metrics":
    import performance_metrics
    performance_metrics.run()
