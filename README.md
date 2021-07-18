# NoteCatcher 📝
NoteCatcher, is a dynamic website for notes.

Add your notes and never forget anything, Delete them when your task is over.

It's a flask app connected to Firebase Real-Time Database.

Hosted on Azure App Service

## Project directory layout

    .
    ├── app.py                # Main App ~ Flask App
    ├── auth.py               # Database Communicator ~ Firebase Authentication  
    ├── template              # Html Pages ~ Jinja Templates
    │   ├── index.html
    │   ├── login.html
    │   ├── signup.html
    │   ├── 404.html
    │   ├── template.html
    │   └── success.html
    │ 
    ├── static               # Images, CSS, JS
    │   ├── style.css
    │   ├── SVG/Images
    │   └── script.js
    │
    ├── requiremnts.txt      # Python Modules required for running the App
    └── README.md

## Live

[NoteCatcher](https://notes.whoisansh.tech). `Azure App Service`

Hosted usign Azure's App Service
* Flask App
* Firebase Authentication
* Firebase Real-Time Database

## How to Run

After Cloning the Code Files on Your PC

Change current directory in the command prompt / Terminal
```
cd NoteCatcher
```

Now Follow These Steps !!!

1. Installing Python Requirements

Install all modules by replacing `<module>`
``` 
pip3 install <module>
```
OR

Install all modules specified in requirements.txt
``` 
pip3 install -r requirements.txt
```
2. adding your Configurations in auth.py

* Go to [Firebase](https://console.firebase.google.com/project/) `Login Required` 
* Create a Project
* Create a Web App  
<img src="/screenshots/fb/fb-add-app.png" alt="drawing" width="300"/>

* Register your App and Copy Config Details to Your [auth.py](https://github.com/26ANSH/NoteCatcher/blob/main/auth.py) `Paste it here in " " `
<img src="/screenshots/fb/fb-app.png" alt="drawing" width="300"/>
<img src="/screenshots/fb/fb-config.png" alt="drawing" width="300"/>

* enable Authenticate from Firebase Authentication
<img src="/screenshots/fb/fb-enable-auth.png" alt="drawing" width="300"/>

* GoTo Firebase Realtime Database and add a Database for your app

3. You are All Set up to Strt your App
```
python3 app.py
```

## App Demo

1. Landing Page
<img src="/screenshots/index.png" alt="drawing" width="300"/>

2. Login/signup ~ Unique Email id linked to Firebase Auth
<img src="/screenshots/login.png" alt="drawing" width="300"/>

3. Notes ~ Linked to Firebase Realtime Databse
<img src="/screenshots/notes.png" alt="drawing" width="300"/>

4. Adding and Deleting Notes With Notifications 
<img src="/screenshots/add.png" alt="drawing" width="300"/>
<img src="/screenshots/delete.png" alt="drawing" width="300"/>

5. Logout ~ once looged in/logged out the app remembers it
<img src="/screenshots/logout.png" alt="drawing" width="300"/>

6. Error Handling 
<img src="/screenshots/404.png" alt="drawing" width="300"/>

### Future Plans

-> Upgrading this app to a custom UI without the Bootstrap ~ Vanilla CSS.

-> A Faster Backend with more features like Email Verfifivation, Calender Support, custom notifications, improved privacy, UI themes, Team notes and much more.

-> Transforming backend from Flask To maybe MERN or Django
