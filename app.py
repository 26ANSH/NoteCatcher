from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

def error404(e):
    return render_template('404.html')

app.register_error_handler(404, error404)

if __name__ == '__main__':
    app.run(debug=True)