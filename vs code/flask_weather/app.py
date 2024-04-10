from flask import Flask, render_template,request
import requests

app = Flask(__name__)

def get_weater(data):
    key = '65731655b56a43f1aca63245240304'
    location = data
    parameters = f'?key={key}&q={location}&aqi=no&days=10'
    link = f'https://api.weatherapi.com/v1/forecast.json{parameters}'
    
    response = requests.get(link)
    
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['location'])
        location = request.form['location']
        data = get_weater(location)
    else:
        print('no location')
        location = "London"
        data = get_weater(location)


    return render_template('index.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)