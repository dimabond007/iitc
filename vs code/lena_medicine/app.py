from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    page='homepage.html'
    return render_template('index.html',page=page)

if __name__ == '__main__':
    app.run(debug=True)