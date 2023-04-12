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

db.child("raspiDeneme").set(121)

data=db.child("raspiDeneme").get()
print(data.val())