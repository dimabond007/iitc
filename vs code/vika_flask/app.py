from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    page = 'homepage.html'
    image_hero = 'homepage_banner.jpg'
    return render_template('index.html',page = page,image_hero=image_hero)

@app.route('/leistungen')
def leistungen():
    page = 'leistungen.html'
    image_hero = 'homepage_banner.jpg'
    return render_template('index.html',page = page,image_hero=image_hero)

@app.route('/über-uns')
def uber_uns():
    page = 'uber_uns.html'
    image_hero = 'uber_uns.png'
    content_hero = 'Über uns'
    
    table_price = {
        {
            'Waschen, schneiden, stylen':'ab 32,- €',
            'Schneiden, trocken':'ab 23,- €',
            'Hochstecken':'ab 40,- €',
            'Flechten':'ab 12,- €',
            'Locken':'	ab 20,- €',
            'Ansatz färben':'	35,- €',
            'Farben (schneiden, selber föhnen)':'	ab 50,- €',
            'Ombré, Balayage, Airtouch':'	ab 100,- €',
            'Strähnen':'	ab 40,- €',
            'Strähnen komplett (Strähnen, Tönung, Föhnen)':'	ab 75 €',
            'Dauerwelle	':'ab 70,- €',
            'Tönung, waschen':'	ab 30,- €',
            'Styling/Finnisch Produkte gehören dazu':None,
            'Augenbrauen zupfen':'	6,-€',
            'Augenbrauen färben':'	6,-€',
            'Wimpeln färben':'	6,-€'
        },
        {},
        {}}
    
    return render_template('index.html',page = page,image_hero=image_hero,content_hero = content_hero)

if __name__ == '__main__':
    app.run(debug=True)