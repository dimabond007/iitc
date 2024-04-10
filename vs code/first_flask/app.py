from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='John')

@app.route('/service')
def servic():
    return render_template('service.html')

@app.route('/btn_click')
def btn_click():
    
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)