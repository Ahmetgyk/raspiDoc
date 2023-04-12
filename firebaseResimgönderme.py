import base64
import pyrebase


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


with open("test.jpg","rb") as img_file:
    my_string=base64.b64encode(img_file.read())
    
print(my_string)
print(my_string.decode("utf-8"))

print("-------")
db.child("raspiResim_utf-8").set(my_string.decode("utf-8"))
data=db.child("raspiResim_utf-8").get()
print(data.val())