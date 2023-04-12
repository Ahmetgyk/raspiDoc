import cv2
import base64
import pyrebase
import time


firebaseConfig = {
  "apiKey": "AIzaSyBJcx5gGKBkxmenIGujYzCRZ786hz5U1B4",
  "authDomain": "marko2-2e536.firebaseapp.com",
  "databaseURL": "https://marko2-2e536-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "marko2-2e536",
  "storageBucket": "marko2-2e536.appspot.com",
  "messagingSenderId": "690586791319",
  "appId": "1:690586791319:web:f79f513965f5a89e83a8d2"
}
 
firebase =pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
 
 
kamera=cv2.VideoCapture(0)

kamera.set(3,640)
kamera.set(4,480)
 

while kamera.isOpened():
 
    ret,kare=kamera.read()
 
    if ret== True:
 
        kare=cv2.flip(kare,0)
 
        cv2.imshow("resim",kare)
 
        basilanTus=cv2.waitKey(1)&0xFF
 
        
        ret,buf=cv2.imencode(".jpg",kare)
        jpg_as_text=base64.b64encode(buf).decode("utf-8")
        db.child("raspiResim_utf-8").set(jpg_as_text)
        print(jpg_as_text)
 
        if basilanTus==ord('x'):
            break
    print("dnene")
    time.sleep(.5)
    
cv2.destroyAllWindows();
 
exit()