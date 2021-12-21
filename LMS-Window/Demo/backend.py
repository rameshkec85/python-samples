import requests
from flask import *
import traceback
app=Flask(__name__)
import library
import json

@app.route('/home-api')
def home(): 
    return "HOME PAGE"

#1. LOGIN/SIGNUP
#2. Add books 
#3. View Books
#4. View Users(Students)
#5. Issue Book 
#6. Request a Book
#http://localhost:5001/signup?name=Anusha&email=anu@gmai.com&password=123456
@app.route('/signup')
def signup():
    #name,email,password, role=Student
    name=request.args.get('name')
    email=request.args.get('email')
    password=request.args.get('password')
    role='student'
    library.addUser(name=name,email=email,password=password,role=role)
    return  {'code':200,'message': "User created successfully"}  

@app.route('/login')
def login():
    email=request.args.get('email')
    password=request.args.get('password')
    row=library.loginUser(email=email,password=password)
    if row is None:
        return {'code':404, 'message':"Invalid Credentials"}

    return {'code':200,'message': "SUCCESS"} 







@app.route('/users')
def users():
    rows=library.getUsers()
    list=[]
    for row in rows:
        print(row['name'])
        list.append({'name':row[1],'role':row[2]})
    return json.dumps(list)    

if __name__ =='__main__':
    # app.run(debug=True)
    app.run(host='localhost', port=5001)

