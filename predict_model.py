# importing the previous trained model 
from train_model import abhi_model
from friends_trainmodel import friends_model
import cv2
import numpy as np
import os

def confidence_percentage(results , image):
    if results[1] < 500 :
        confidence = int( 100 * (1 - (results[1])/400) )
        display_string = str(confidence) + '% Confident It Human Face .'
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
    return confidence



face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is () :
        return img, []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

# Open Webcam
cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    image, face = face_detector(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        my_results = abhi_model.predict(face)
        friend_results = friends_model.predict(face)

        my_results_confidence = confidence_percentage(my_results , image )
        friend_results_confidence = confidence_percentage(friend_results , image )
        

        if my_results_confidence > 80:
            cv2.putText(image, "Hey Abhishek  ", (180, 380), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
            cv2.imshow('Face Recognition', image )
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
            try:
                import pywhatkit as kit
                #sending mail

                kit.send_mail("abhishekdwibedy1@gmail.com" , #sender mailaddress
                              "Abhishek@2002" ,              #password of sender Mail id
                              "!! SECURITY ALERT !!" ,       # Subject Of Email that to send to receiver
                              "Hey Abhishek..  Your Face has Been Detected In WebCamera." ,        #Message 
                              "dwibedyabhishek1@gmail.com")   #Receiver emailaddress
                print("Email Sent Successfully !!!")


                #sending Whatsup Message 
                
                p_num = input("Enter the Phone Number To whome U want to send Message [In the form +91 (Ex-+9183********)] : -")
                message = input("Enter The Message U want to send :-")
                # Syntax: pywhatkit.sendmsg(“receiver mobile number”,”message”,hours,minutes)
                # NOTE: This module follows the 24 hrs time format.
                kit.sendwhatmsg(p_num, message, 3 , 50)
                print("Whatsup Message Sent Successfully !!!")
                break

            except: 
                print("Unable To send Message ")
                break

        elif friend_results_confidence > 80:

            cv2.putText(image, "Launching EC2Instance nd Attaching ", (180, 380), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
            cv2.putText(image, "EBS Volume of 5GB to it after creation.   ", (210, 410), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
            cv2.imshow('Face Recognition', image )
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
            try:

                import pywhatkit as kit

                kit.send_mail("abhishekdwibedy1@gmail.com" , #sender mailaddress
                              "Abhishek@2002" ,              #password of sender Mail id
                              "!! SECURITY ALERT !!" ,       # Subject Of Email that to send to receiver
                              "A Face Has Been Detected In Your WebCamera" ,        #Message 
                              "dwibedyabhishek1@gmail.com")   #Receiver emailaddress
                print("Email Sent Successfully !!!")

                os.system("terraform init")
    # terraform code to launch a website on AWS with permanent EBS storage mounted. 
                os.system("terraform apply --auto-approve")

                print(" AWS EC2 Instance Successfully created and 5GB EBS Volume is attched to it.")
                break

            except:
                print("Error in Terraform file.")
                break

            

        else:    
            cv2.putText(image, "Rcognizing Face...", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
        
    except:
        cv2.putText(image, "No Face Found!", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "Looking For Face...", (220, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass
        
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()  



