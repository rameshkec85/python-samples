from os import name
from sqlite3.dbapi2 import Cursor

from requests.api import request
from flask import *
import requests
import sqlite3

from LMSDb import LMSDB
con = sqlite3.connect('users.db',check_same_thread=False)
import traceback
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',name="Admin")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

#JSON: 
#/validateLogin?email=&password=
@app.route('/validateLogin')
def validateLogin():
     email=request.args.get('email')
     password=request.args.get('password')

     if email=='demo' and password=='123':
        #  return render_template('dashboard.html',name=email)
        return redirect(url_for('dashboard',name=email))

     return "Login Error"  

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',name=request.args.get('name'))

    #  return {'email':email,'password':password};


@app.route("/hello")
def hello():
     return """ 
    <body><h1>Hello</h1>
    <input type='text' placeholder='name'/>
    <input type='password' placeholder='Password'/>
    <input type='button' value='Submit'/>
    </body>
    """


#DATABASE START
@app.route('/users')
def users():
    # return render_template('user.html',users=[{'name':'Ramesh'},{'name':'Laxman'},{'name':'Ganesh'}])
    return render_template('user.html',users=getUsers())

def createTables():
    cur = con.cursor()
    cur.execute('''CREATE TABLE if not exists users
               (id integer primary key,
               name text
               )''')
    con.commit()

def addDummyData():
    try:
         cur = con.cursor()
        #  cur.execute("""insert into users(id,name) values(1,'Ramesh')""")
         cur.execute("""insert into users(id,name) values(2,'Laxman')""")
         cur.execute("""insert into users(id,name) values(3,'Ganesh')""")
         cur.execute("""insert into users(id,name) values(1,'Ramesh')""")
         con.commit()
    except Exception as e:
        print(traceback.format_exc())   
        con.commit()
        print('Exception in addDummyData')   

@app.route('/getusers')
def getUsers():
    with app.app_context():
        try:
            # print(request.url)
            cur=con.cursor()
            rows=cur.execute('select * from users')
            users=[]
            for row in rows:
                print(str(row[0])+", "+row[1])
                users.append({'id':row[0],'name':row[1]})

            # return jsonify(users)
            return users
        except Exception as e:
            print(e)
            return "Error"
# LMSDB
@app.route('/testdbusers')
def testdbusers():
    db=LMSDB(app=app)
    return db.getAllUsers()

@app.route('/adduser/<name>')
def adduser(name):
    db=LMSDB(app=app)
    id=request.args.get('id')
    message=db.addRecord(id,name)
    return message



#DATABASE END
import json
import datetime
#External service
@app.route('/weather/<city>')
def callWeatherApi(city):
    #
    apiKey=request.args.get('key')
    data=requests.get('https://api.openweathermap.org/data/2.5/forecast?appid='+apiKey+'&units=metric',params={'q':city})
    d = json.loads(data.text)
    temp=d['list'][0]['main']['temp']
    #=====
    list=[] 

    for temp in d['list']:
        time=temp['dt_txt'] #date 
        temp=temp['main']['temp'] #temperature 2021-12-12 21:00:00
        fdate=datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S').strftime('%d %b %I %p')
        list.append({'time':time, 'temp':int(temp),'ftime':fdate})
        
        
    return render_template('weather.html',weatherlist=list)    
    # return json.dumps(list)
    #======
    # print(temp)
    # return {'temp':temp}


@app.route('/city/<mycity>')
def mycity(mycity):
    return mycity


#======= 

def dateFormateExample():
    #Date format (date object to desired date as string) (object ->string )
    ctime=datetime.datetime.now()
    ftime=datetime.datetime.strftime(ctime,'%d/%m/%y %H:%M %p') #12/12/21 16:27 PM
    print(ftime)

    #Date parse (string -> object)
    datestr='12/12/21 16:27 PM'
    dateObj=datetime.datetime.strptime(datestr,'%d/%m/%y %H:%M %p')

@app.route('/userslist/<int:page>')    
def callUsers(page):
    rq=requests.get('https://reqres.in/api/users?page='+str(page)+'&per_page=10')
    #users-list.html
    return render_template('users-list.html',users=json.loads(rq.text)['data'])





if __name__ =='__main__':
    dateFormateExample()
    createTables();
    addDummyData()
    app.run(debug=True)



#development - server
#production - server     


    
