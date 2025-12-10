# Task-05: Face Detection using OpenCV

## Objective
Implement a face detection system using Python and OpenCV. The goal is to load an image, detect human faces, and highlight them with bounding boxes.

## Steps
1. Imported OpenCV (`cv2`) and loaded the Haar Cascade Classifier (`haarcascade_frontalface_alt.xml`).
2. Read the input image (`test.jpg`) and converted it to grayscale.
3. Applied `detectMultiScale()` to locate faces in the image.
4. Drew rectangles around detected faces.
5. Displayed the output using `cv2.imshow()` and saved the result (`detected_output.jpg`) for proof.

## Output
- The script successfully detects faces in the image.
- Bounding boxes are drawn around each detected face.
- Output can be viewed in the saved image or live window.

## Skills Demonstrated
- Computer Vision basics
- Image preprocessing
- Haar Cascade Classifier usage
- Python + OpenCV workflow

## Demo
![Face Detection Output](detected_output.jpg)

