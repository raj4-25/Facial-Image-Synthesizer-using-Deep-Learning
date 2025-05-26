# Facial-Image-Synthesizer-using-Deep-Learning
## Project Overview
Facial expressions form a fundamental aspect of human communication, offering a non-verbal channel for 
conveying emotions and social cues. The advent of artificial intelligence (AI) and computer vision has 
opened new frontiers in recognizing and synthesizing facial expressions. This project presents a real-time 
facial expression manipulation system that captures live images from a webcam, processes them via a 
third-party expression editor API (Segmind), and produces visually altered facial expressions.

The system is designed using modular Python scripts for individual emotions—angry, happy, sleepy, and 
surprised—and is supplemented with a desktop-based GUI launcher for usability. Captured images are 
encoded in base64 and transmitted with parametric configurations to control specific facial features such 
as mouth shape, eyebrow positioning, eye movements, and head orientation. The API responds with a 
processed image reflecting the desired emotional state, which is then stored and optionally displayed to 
the user. 

## Facial Landmark Detection using OpenCV:  
Finding particular important areas on a person's face, like the corners of their eyes, nose, 
and mouth, as well as other facial features, is a fundamental job in the field of computer vision 
known as facial landmark detection.

## Aim and Objective  
● To build a real-time facial expression manipulation system.  
● To utilize a third-party API for expression synthesis, avoiding local model  training.  
● To support modular expression types through parameterized payloads.  
● To develop a GUI launcher for ease of use and accessibility.  
● To store and display both input and output images for comparison.  

## ALGORITHM 
Algorithm: Facial Expression Synthesis & Manipulation 
1. Initialize System 
Set up camera input (e.g., webcam or mobile camera). 
Initialize connection to an image processing API (e.g., OpenCV, Dlib, MediaPipe, or 
cloud APIs like Face++ or Microsoft Face API). 
2. Capture Frame 
Continuously capture frames from the camera feed. 
Convert frame to RGB (if needed by API). 
python 
frame = camera.read() 
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
3. Detect Face and Extract Landmarks 
Use the API to detect the face and extract facial landmarks (e.g., 68-point Dlib or 
MediaPipe landmarks). 
python 
landmarks = face_api.get_landmarks(rgb_frame) 
4. Analyze Expression (Optional) 
(Optional) Use a pre-trained model to detect the current facial expression (e.g., happy, sad,angry)
5. Synthesize or Manipulate Expression 
Use either: 
Blendshape models to adjust landmarks (e.g., move mouth corners to simulate a smile). 
GAN-based models (e.g., GANimation, StyleGAN) to generate a new image with the 
desired expression. 
Pass modified landmarks or latent vectors to the model/API. 
python 
modified_landmarks = apply_expression_modification(landmarks, target_expression) 
synthetic_image = generate_image_with_expression(rgb_frame, modified_landmarks) 
6. Render or Display Output 
Blend the synthesized face back onto the original frame (if necessary). 
Display or return the new image. 
python 
cv2.imshow('Modified Expression', synthetic_image) 
7. Loop or Terminate 
Repeat steps 2–6 in a loop or terminate based on user input.


