import cv2
import numpy as np
from ultralytics import YOLO
import pyttsx3
import math
import threading
import time
import cvzone
import streamlit as st

# Initialize global variables and model
model = YOLO("streamlit_app/best.pt")
classNames = model.names
#warning message
warning_message="wear your personal protective equipment!"
#last warning time
last_warning_time=time.time()
#warning interval
warning_interval=5 #seconds
# Initialize the speech engine
engine = pyttsx3.init()



def speak_warning():
    engine.say(warning_message)
    engine.runAndWait()

def process_frame(img, confidence_threshold):
    global last_warning_time

    results = model(img, stream=True)
    
    # Initialize person_color to a default value
    person_color = (0, 255, 0)  # Default green if PPE is worn

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            confidence = math.ceil(box.conf[0] * 100)
            
            if confidence >= confidence_threshold:
                if classNames[cls] == "person":
                    x1, y1, x2, y2 = list(map(int, box.xyxy[0]))

                    helmet_boxes = []
                    vest_boxes = []
                    
                    for inner_box in boxes:
                        inner_cls = int(inner_box.cls[0])
                        inner_x1, inner_y1, inner_x2, inner_y2 = list(map(int, inner_box.xyxy[0]))
                        
                        if (inner_x1 >= x1 and inner_x2 <= x2 and inner_y1 >= y1 and inner_y2 <= y2):
                            if classNames[inner_cls] == "helmet":
                                helmet_boxes.append(inner_box)
                            elif classNames[inner_cls] == "vest":
                                vest_boxes.append(inner_box)

                    if len(helmet_boxes) == 0 or len(vest_boxes) == 0:
                        # Update person_color to red if PPE is not worn
                        person_color = (0, 0, 255)  # Red color for no PPE
                        current_time=time.time()
                        
                        if current_time - last_warning_time >= warning_interval:
                            t1=threading.Thread(target=speak_warning)
                            t1.start()
                            last_warning_time = current_time
                    else:
                        # Green color for wearing PPE (default value set earlier)
                        person_color = (0, 255, 0)        

                    # Draw a rectangle around the person
                    cv2.rectangle(img, (x1, y1), (x2, y2), person_color, 2)
                    # Display person and confidence
                    cvzone.putTextRect(img, f'Person {confidence}%', (x1, y1 - 10), scale=1, thickness=2, offset=5, colorR=person_color)

                    # Draw rectangles around the helmet and vest boxes
                    for helmet_box in helmet_boxes:
                        helmet_x1, helmet_y1, helmet_x2, helmet_y2 = list(map(int, helmet_box.xyxy[0]))
                        cv2.rectangle(img, (helmet_x1, helmet_y1), (helmet_x2, helmet_y2), (255, 94, 77), 2)
                        # Display helmet and confidence
                        cvzone.putTextRect(img, f'Helmet {math.ceil(helmet_box.conf[0] * 100)}%', 
                                           (helmet_x1, helmet_y1 - 10), scale=1, thickness=2, offset=5, colorR=(255,94,77))

                    for vest_box in vest_boxes:
                        vest_x1, vest_y1, vest_x2, vest_y2 = list(map(int, vest_box.xyxy[0]))
                        cv2.rectangle(img, (vest_x1, vest_y1), (vest_x2, vest_y2), (7, 255, 170), 2)
                        # Display vest and confidence
                        cvzone.putTextRect(img, f'Vest {math.ceil(vest_box.conf[0] * 100)}%', 
                                           (vest_x1, vest_y1 - 10), scale=1, thickness=2, offset=5, colorR=(7, 255,170))

    return img

