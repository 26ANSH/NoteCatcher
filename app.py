from flask import Flask, render_template, request, redirect, session, jsonify
from auth import new_user, Login, get_notes, add_note, remove_note
import json

app = Flask(__name__)
app.secret_key='put_anything _that_you_want'

@app.route('/')
def hello():
    if 'Logged_in' not in session:
        return render_template('index.html')
    else:
        return redirect('/notes')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'Logged_in' in session:
        number,notes = get_notes(session['User_id'])
        return render_template('notes.html',number = number,notes = notes)
    else:
        return render_template('login.html',color='danger', error='Please Login to Access your Notes')

@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == '' or password == '':
            return render_template('signin.html', error='Please Fill all Details')

        if len(password) <6:
            return render_template('signin.html', error='Password should be at least 6 characters')

        call, msg = new_user(email, password)

        if call == 0:
            session.clear()
            session['Logged_in'] = email
            session['User_id'] = msg
            return render_template('success.html',email=email)
        else:
            return render_template('signin.html', error=msg)
    else:
        if 'Logged_in' not in session:
            return render_template('signin.html',error='')
        else:
            return redirect('/notes')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == '' or password == '':
            return render_template('login.html',color='danger', error='Please Fill all Details')

        call, msg = Login(email, password)

        if call == 0:
            session.clear()
            session['Logged_in'] = email
            session['User_id'] = msg
            return redirect("/notes")
        else:
            return render_template('login.html', error=msg)
    else:
        if 'Logged_in' not in session:
            return render_template('login.html', error='')
        else:
            return redirect('/notes')

@app.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    remove_note(session['User_id'], note['noteid'])
    return jsonify({})

@app.route('/add-note', methods=['POST'])
def add_notes():
    note = json.loads(request.data)
    print(note['note_data'])
    id = add_note(session['User_id'], note['note_data'])
    return jsonify({'noteid':id})

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    session['Logged_out'] = 'ok'
    return jsonify({})

def error404(e):
    return render_template('404.html')

app.register_error_handler(404, error404)
app.register_error_handler(405, error404)
app.register_error_handler(500, error404)

if __name__ == '__main__':
    app.run(debug=True)