import RPi.GPIO as GPIO
import time
import pyrebase

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print ("HC-SR04 mesafe sensoru")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


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


while True:

 GPIO.output(TRIG, False)
 print ("Olculuyor...")
 time.sleep(2)

 GPIO.output(TRIG, True)
 time.sleep(0.00001)
 GPIO.output(TRIG, False)

 while GPIO.input(ECHO)==0:
     pulse_start = time.time()

 while GPIO.input(ECHO)==1:
     pulse_end = time.time()

 pulse_duration = pulse_end - pulse_start

 distance = pulse_duration * 17150
 distance = round(distance, 2)

 if distance > 2 and distance < 400:
     db.child("raspiDeneme").set(distance)
     data=db.child("raspiDeneme").get()
     print ("Mesafe:",data.val() - 0.5,"cm")
 else:
     print ("Menzil asildi")
