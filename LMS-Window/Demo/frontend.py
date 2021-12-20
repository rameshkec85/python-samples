import requests
from flask import *
import traceback
app=Flask(__name__)

BASE_URL='http://localhost:5001'

@app.route('/home')
def home():
    res=requests.get(BASE_URL+'/home-api')
    return render_template('home.html',name=res.text)



@app.route('/dashboard')
def home():
    res=requests.get(BASE_URL+'/dashboard-api')
    return render_template('home.html',name=res.text)



if __name__ =='__main__':
    app.run(debug=True)