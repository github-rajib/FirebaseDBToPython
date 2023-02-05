
"""Connecting Firebase Realtime Database To Python: Creating, Reading, Updating, and Deleting Data"""
# imports
import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyCvnBFRU41p_12ogVJNsEcSSvJBLfWHhpw",
    "authDomain": "connectingfirebasedbtopy-6ea82.firebaseapp.com",
    "projectId": "connectingfirebasedbtopy-6ea82",
    "databaseURL": "https://connectingfirebasedbtopy-6ea82-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": "connectingfirebasedbtopy-6ea82.appspot.com",
    "messagingSenderId": "73626561560",
    "appId": "1:73626561560:web:dfe799840c9e65961fa76d",
    "measurementId": "G-XHGE8GG001"
}


firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

data = {"name": "Rakib", "age": 25, "location": "Barishal, Bangladesh", "Like pizza": True}

"""Create Data -------------------------------------------------------------------------------------------------------------"""
# database.push(data)
# response = database.child("Users").child("FirstPersion").set(data)


"""Read Data ----------------------------------------------------------------------------------------------------------------"""
# response = database.child("Users").child("FirstPersion").get()
# print("response :", response.val())


"""Update Data --------------------------------------------------------------------------------------------------------------"""
# response = database.child("Users").child("FirstPersion").update({"age": 30})
# print("response :", response)


"""Delete Data --------------------------------------------------------------------------------------------------------------"""
# delete 1 value
# response = database.child("Users").child("FirstPersion").child("age").remove()
# delete whole node
# response = database.child("Users").child("FirstPersion").remove()
# print("response :", response)
