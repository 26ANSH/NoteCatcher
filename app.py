from flask import Flask, render_template, request, redirect
from auth import new_user, sign_in

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/user')
def success():
    return render_template('success.html')

@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        call = new_user(email, password)
        if call == 0:
            return redirect("/user")
        else:
            return render_template('signin.html',color='danger', error=call)
    else:
        return render_template('signin.html',color='success',error='Signin with valid Email ID')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        call = sign_in(email, password)
        if call == 0:
            return redirect("/user")
        else:
            return render_template('login.html',color='danger', error=call)
    else:
        return render_template('login.html',color='success', error='Login with valid Email ID')

def error404(e):
    return render_template('404.html')

app.register_error_handler(404, error404)

if __name__ == '__main__':
    app.run(debug=True)