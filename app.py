from flask import Flask

from flask import render_template , request , redirect, Response


app = Flask(__name__)



@app.route('/')
def home(): 
    active=['active','',''] 
    return render_template('homicidios/index.html',active=active)

@app.route('/about')
def about():
    active=['','active','']
    return render_template('homicidios/about.html',active=active)

@app.route('/statistics')
def statistics():
    active=['','','active'] 
    return render_template('homicidios/statistics.html',active=active)



if __name__=='__main__':
    app.run(debug=True)