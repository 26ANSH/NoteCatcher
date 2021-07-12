import pyrebase
import requests
import json

CONFIG = {
    "apiKey" : "AIzaSyAGXobNG-hC6ufs4eV-ca1KMo5k-FEAusA",
    "authDomain" : "firecatchers-task-2.firebaseapp.com",
    "databaseURL" : "https://firecatchers-task-2-default-rtdb.firebaseio.com",
    "projectId" : "firecatchers-task-2",
    "storageBucket" : "firecatchers-task-2.appspot.com",
    "messagingSenderId" : "664983494868",
    "appId" : "1:664983494868:web:e4eb6e31cb509f03535b41"
  }

firebase = pyrebase.initialize_app(CONFIG)
auth = firebase.auth()

def new_user(email, password):
  try:
    auth.create_user_with_email_and_password(email, password)
  except requests.HTTPError as e:
    error_json = e.args[1]
    error = json.loads(error_json)['error']['message']
    if error == "EMAIL_EXISTS":
      return 'Email Already Exists, Try Again'
  else:
    return 0

def sign_in(email, password):
  try:
    auth.sign_in_with_email_and_password(email, password)
  except requests.HTTPError as e:
    error_json = e.args[1]
    error = json.loads(error_json)['error']['message']
    if error == "INVALID_EMAIL":
      return 'Email is not registered, Try again'
    else:
      return 'Wrong Password Try again'
  else:
    return 0