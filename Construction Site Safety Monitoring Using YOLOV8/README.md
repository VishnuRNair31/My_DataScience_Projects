#  Construction Site Safety Monitoring Using YOLOv8 
![image](https://github.com/VishnuRNair31/My_DataScience_Projects/blob/main/Construction%20Site%20Safety%20Monitoring%20Using%20YOLOV8/image.jpg?raw=true)
This project aims to enhance workplace safety on construction sites by using a deep learning model to monitor workers and ensure compliance with Personal Protective Equipment (PPE) regulations. The system leverages the YOLOv8 object detection model to identify individuals and detect whether they are wearing safety gear such as helmets and vests in real-time. This ensures a proactive approach to safety by providing instant feedback through sound warnings when violations are detected.

## Features
YOLOv8 for Object Detection: The Ultralytics YOLOv8 model is used for fast and accurate detection of workers and PPE (helmets and vests) in both live video streams and image inputs.
Real-time Monitoring: A webcam or video feed is used to monitor workers on construction sites in real-time. The system checks for PPE compliance at defined intervals.
Safety Violation Alerts: If a worker is not wearing the required safety gear, an audible alert (sound warning) is triggered to notify them immediately.
Streamlit Frontend: A user-friendly interface developed using Streamlit allows for easy setup and monitoring. Users can start live detection and review PPE compliance directly from the browser.
Integration with OpenCV and Pyttsx3: OpenCV is used for video processing, while pyttsx3 is utilized to generate sound warnings.
CVzone for Streamlined Interface: The project incorporates the CVzone library to assist with real-time detection and display of results on the screen.

## Technologies Used
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy
* Streamlit
* Pyttsx3
* CVzone
## How It Works
* Model Training: A YOLOv8 model is trained on a dataset containing images of workers wearing and not wearing PPE (helmets and vests).
* Live Detection: The application utilizes a webcam feed to continuously monitor workers, identifying individuals and checking for PPE compliance.
* Safety Check: The system checks at regular intervals whether each worker is complying with PPE requirements.
* Violation Alert: If a violation is detected (e.g., a worker not wearing a helmet), the system issues a sound warning to alert the worker and prompt corrective action.

## Future Improvements
* Transfer Learning: Improve the model's accuracy by incorporating transfer learning techniques.
* Extended PPE Detection: Expand the system to detect additional PPE items such as gloves, goggles, or boots.
* Cloud Integration: Implement cloud storage and real-time data reporting for better monitoring and analysis.
