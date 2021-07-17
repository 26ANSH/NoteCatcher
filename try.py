import pyrebase
import time

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
db = firebase.database()

user = db.child('nJLWaqLIZNZj7pEA8WF8NpenAP42').push('hello i am here')
print(user['name'])