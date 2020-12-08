# DinoPlay
Play chrome Dino with your smile! Used lib OpenCv.

# How it works?
OpenCv library has pretrained Haar cascade models. At first we are detecting face. If face is detected, we are looking for a smile.
When we are smiling Dino is happy so he jumps! Now we can play Dino without touching keyboard!

# 1. Open new Chrome tab with Dino game.
![s1](https://user-images.githubusercontent.com/69935274/101422420-f183f780-38f6-11eb-8079-be2bb4d9c847.png)

# 2. Initialize pretrained Haar model.
In variable "cap" we define which camera we will be using. <br>
![s2](https://user-images.githubusercontent.com/69935274/101422441-ff397d00-38f6-11eb-86dd-0be6bbae4b97.png)

# 3. While loop.
We use while(True) loop for continous capturing frames from camera
![s3](https://user-images.githubusercontent.com/69935274/101422460-08c2e500-38f7-11eb-886f-2eb5bdaf7a54.png)

# 4. Function detectMultiScale() is used to detect faces.
This function works only on black-white frames so we have to convert RGB frame.
![s4](https://user-images.githubusercontent.com/69935274/101422482-11b3b680-38f7-11eb-929e-04d2847993f3.png)

# 5. Drawing rectangle on detected face.
If face is detected, variable faces will contains table with [X_up_left_corner,Y_up_left_corner, Width_of_face, Height_of_face]
X of the down right corner = X_up_left_corner + Width_of_face
Y of the down right corner = Y_up_left_corner + Height_of_face
![s5](https://user-images.githubusercontent.com/69935274/101422508-1bd5b500-38f7-11eb-91b8-96bb7eaa8f85.png)

# 6.Crop out detected face for smile detection.
For smile detection, face have to be in black-white as well.
![s6](https://user-images.githubusercontent.com/69935274/101422572-4162be80-38f7-11eb-83e7-69546020fac3.png)

# 7. Drawing rectangle on the detected face.
If smile is detected, code artificially create pressing key "UP". 
![s7](https://user-images.githubusercontent.com/69935274/101422598-54758e80-38f7-11eb-8aff-d5070e809ec4.png)

# 8. After all detection and drawing we have to show image in a frame.
If we want to break the loop we press 'Q'
![s8](https://user-images.githubusercontent.com/69935274/101422605-5b040600-38f7-11eb-82be-3c84f9a65cd3.png)

# 9. When everything done, release the capture. 
![s9](https://user-images.githubusercontent.com/69935274/101422617-5fc8ba00-38f7-11eb-9e86-63a38e81ebe8.png)

# Me playing Dino:
https://www.youtube.com/watch?v=aYPh4HTYxdc
