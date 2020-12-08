# DinoPlay
Play chrome Dino with your smile! Used lib OpenCv.

# How it works?
OpenCv library has pretrained Haar cascade models. At first we are detecting face. If face is detected, we are looking for a smile.
When we are smiling Dino is happy so he jumps! Now we can play Dino without touching keyboard!

# 1. Open new Chrome tab with Dino game.
# 2. Initialize pretrained Haar model.
In variable "cap" we define which camera we will be using. 
# 3. While loop.
We use while(True) loop for continous capturing frames from camera
# 4. Function detectMultiScale() is used to detect faces.
This function works only on black-white frames so we have to convert RGB frame.

# 5. Drawing rectangle on detected face.
If face is detected, variable faces will contains table with [X_up_left_corner,Y_up_left_corner, Width_of_face, Height_of_face]
X of the down right corner = X_up_left_corner + Width_of_face
Y of the down right corner = Y_up_left_corner + Height_of_face

# 5.Crop out detected face for smile detection.
For smile detection, face have to be in black-white as well.


# 6. Drawing rectangle on the detected face.
If smile is detected, code artificially create pressing key "W". 

# 7. After all detection and drawing we have to show image in a frame.
If we want to break the loop we press 'Q'

# 8. When everything done, release the capture. 

# Me playing Dino:
https://www.youtube.com/watch?v=aYPh4HTYxdc
