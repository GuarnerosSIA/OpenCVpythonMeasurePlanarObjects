import cv2

cam = cv2.VideoCapture(0)
#Camera parameters
cam.set(11,0)
cam.set(3,640) #Width
cam.set(4,480) #Height

cv2.namedWindow("Preview")
#Create a window to preview the images

img_calibration = 0
#Creates the calibration numerator to take images

while True:
    ret, frame = cam.read()#take a picture
    #Verify if the image was taken
    if not ret:
        print("failed to grab frame")
        break #Exit the application
    
    cv2.imshow("Preview", frame)
    #Show the image in the created window
    k = cv2.waitKey(1)
    #Wait for a key commans every milisecond
    #If a key is pressed, the following condition are asked
    if k%256 == 27:
        print("Calibration Image Adquisition Finished")
        break
    elif k%256 == 32:
        img_name = "chessboard images\\11x8\\Calibration{}.png".format(img_calibration)
        cv2.imwrite(img_name, frame)
        print("{} saved!".format(img_name))
        img_calibration += 1
        

cam.release()

cv2.destroyAllWindows()