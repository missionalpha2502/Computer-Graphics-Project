from io import BytesIO

import cv2
from cv2.dnn import imagesFromBlob
import numpy as np
import requests

# Read the input image from URL
url = 'https://replit.com/@missionalpha250/COmputer-Graphics-Project#images.jpeg'

response = requests.get(url)
if response.status_code == 200:
    # Decode image content into a NumPy array
    img = cv2.imdecode(np.frombuffer(response.content, np.uint8),
                       cv2.IMREAD_COLOR)

    # Check if the image is loaded successfully
    if img is not None:
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Save the processed image
        cv2.imwrite('output.jpg', gray_img)

        # Read the output image
        with open('output.jpg', 'rb') as f:
            img_data = f.read()

        # Send the processed image to a web server
        upload_url = 'http://your-web-server.com/upload'
        headers = {'Content-Type': 'image/jpeg'}
        response = requests.post(upload_url, data=img_data, headers=headers)

        # Print the server response
        print(response.text)
    else:
        print("Failed to load the image.")
else:
    print("Failed to fetch the image from the URL.")
    print("Response status code:", response.status_code)
    print("Response content:", response.content)
