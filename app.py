from flask import Flask
import requests
from flask import render_template , request , redirect, Response , jsonify


app = Flask(__name__)

#Get GeoJson Api----
url = 'https://python-api-homicidios.herokuapp.com/'
response = requests.get(url).json()

@app.route('/')
def home(): 
    active=['active','',''] 
    return render_template('homicidios/index.html',active=active,response = response)

@app.route('/about')
def about():
    active=['','active','']
    return render_template('homicidios/about.html',active=active)

@app.route('/statistics')
def statistics():
    active=['','','active'] 
    return render_template('homicidios/statistics.html',active=active,response = response)



if __name__=='__main__':
    app.run(debug=True)