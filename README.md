# FireCatchers
This Repo Consists of Solutions to Tasks for the FireQuest Organised by GDG Chandigarh and IEEE CU

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

## Live Demo

[NoteCatcher](https://notes.whoisansh.tech). `Azure App Service`

Hosted usign Azure's App Service
* Flask App
* Firebase Authentication
* Firebase Real-Time Database

## How to Run

After Cloning the Code Files on Your PC

> CD NoteCatcher to set current directory

Now Follow These Steps !!!

1. Installing Python Requirements

Install all modules one by one
``` 
pip3 install 'module'
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
* enable Authenticate from Firebase Authentication

3. You are All Set up

```
python3 app.py
```

#### App Demo

1. Index 

<img src="/screenshots/index.png" alt="drawing" width="300"/>

2. Login/signup 

<img src="/screenshots/login.png" alt="drawing" width="300"/>

3. Notes 

<img src="/screenshots/notes.png" alt="drawing" width="300"/>

4. Adding and Deleting Notes With Notifications 

<img src="/screenshots/add.png" alt="drawing" width="300"/>

<img src="/screenshots/delete.png" alt="drawing" width="300"/>

5. Logout 

<img src="/screenshots/logout.png" alt="drawing" width="300"/>

6. Error Handling 

<img src="/screenshots/404.png" alt="drawing" width="300"/>


