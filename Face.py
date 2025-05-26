

import requests
import base64
from io import BytesIO
from PIL import Image
import cv2
import datetime

# Capture image from USB camera
def capture_image_from_camera_With_camera_Preview():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None
    
    print("Press 'Space' to capture image and 'Esc' to exit preview.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        cv2.imshow('Camera Preview', frame)
        key = cv2.waitKey(1)
        if key == 27:  # Esc key to exit
            break
        elif key == 32:  # Space bar to capture
            cap.release()
            cv2.destroyAllWindows()
            return frame
    
    cap.release()
    cv2.destroyAllWindows()
    return None


# Capture an image from the USB camera and convert to base64
def capture_image_from_camera():
    cap = cv2.VideoCapture(0)  # 0 is usually the default camera
    if not cap.isOpened():
        raise Exception("Could not open camera")
    
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        raise Exception("Failed to capture image")
    
    # Convert the captured frame to bytes
    _, buffer = cv2.imencode('.png', frame)
    return base64.b64encode(buffer).decode('utf-8')

# Use this function to convert an image file from the filesystem to base64
def image_file_to_base64(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return base64.b64encode(image_data).decode('utf-8')

# Use this function to fetch an image from a URL and convert it to base64
def image_url_to_base64(image_url):
    response = requests.get(image_url)
    image_data = response.content
    return base64.b64encode(image_data).decode('utf-8')


# Save captured image with current date-time as filename
def save_captured_image(image):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image_path = f"captured_image_{timestamp}.png"
    cv2.imwrite(image_path, image)
    print(f"Image saved as {image_path}")
    return image_path

# Convert response content into an image and save it
def save_response_image(response):
    try:
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = f"output_image_{timestamp}.png"
        image.save(output_file)
        print(f"Image successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

api_key = "SG_bf69196d5a88fc20"
url = "https://api.segmind.com/v1/expression-editor"

#print(image_url_to_base64("https://URL/ep-editor-ip.png"))
#print(image_file_to_base64("Test.jpg"))

# Capture image from camera
captured_image = capture_image_from_camera_With_camera_Preview()
if captured_image is not None:
    image_path = save_captured_image(captured_image)
    image_base64 = image_file_to_base64(image_path)

# Request payload
data = {
  "aaa":0,
  "blink": 0,
  "eee": 0,
  "eyebrow":1,
  "image": image_base64, 
  "image_format": "png",
  "image_quality": 95,
  "pupil_x": 0,
  "pupil_y": 0,
  "rotate_pitch": 0,
  "rotate_roll": 0,
  "rotate_yaw": 0,
  "sample_parts": "OnlyExpression",
  "smile": 0,
  "wink": 0,
  "woo": 0
}

headers = {'x-api-key': api_key}

response = requests.post(url, json=data, headers=headers)

#print(response.content)  # The response is the generated image
#save_response_image(response, 'output_image_asd.png')
save_response_image(response)
