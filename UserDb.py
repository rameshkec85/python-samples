from flask import *
import sqlite3
app=Flask(__name__)
import json
import traceback
import pandas as pd


con = sqlite3.connect('students.db',check_same_thread=False)
#CRUD Operations 
def createTables():
    try:
        cursor=con.cursor() #varchar
        cursor.execute('create table if not exists students(id integer primary key, name text)')
        con.commit()
    except Exception as e:
        # con.rollback()
        print(e)    

@app.route('/add_student/<int:id>/<name>')
def addStudent(id,name):
    try: 
        #
        with app.app_context():
            cursor=con.cursor() #varchar
            cursor.execute('insert into students(id,name) values(?,?)',(id,name))
            con.commit()
    except Exception as e:
        print(traceback.format_exc())  
    return "Success"  

@app.route('/delete_student/<int:id>')
def deleteStudent(id):
    try:
        with app.app_context():
            cursor=con.cursor() #varchar
            cursor.execute('delete from students where id='+str(id))
            con.commit()
    except Exception as e:
        print(traceback.format_exc())  
    return "Success"   


@app.route('/update_student/<int:id>/<name>')
def updateStudent(id,name):
    try:
        with app.app_context():
            cursor=con.cursor() #varchar
            cursor.execute('update students set name='+name+' where id='+str(id))
            con.commit()
    except Exception as e:
        print(traceback.format_exc())  
    return "Success"             

@app.route('/students')
def getStudents():
    list=[]
    try:
        with app.app_context():
            cursor=con.cursor() #varchar
            rows=cursor.execute('select * from students')
            
            for row in rows:
                print(row[0])#id
                print(row[1]) #name
                list.append({'id':row[0],'name':row[1]})
        return render_template('user.html',users=list)
    except Exception as e:
        print(e)   
    
    return json.dumps(list)
    

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_excel(f,usecols=['Book', 'Author'])
        js=data_xls.to_dict(orient='records')
        print(json.dumps(js))  
        #return data_xls.to_html()
        js=json.dumps(js)
        #====
        #BULK UPLOAD
        #====
        return js
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (xlsx only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    '''


if __name__ =='__main__':
    createTables()
    # addStudent(1,'Kohli')
    getStudents()
    app.run(debug=True)
