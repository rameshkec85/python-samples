import sqlite3
import json
import traceback

con = sqlite3.connect('users.db',check_same_thread=False)

class LMSDB:
    
    def __init__(self,app):
        self.app=app

    def getAllUsers(self):
        with self.app.app_context():
            try:
                # print(request.url)
                cur=con.cursor()
                rows=cur.execute('select * from users')
                users=[]
                for row in rows:
                    print(str(row[0])+", "+row[1])
                    users.append({'id':row[0],'name':row[1]})

                print(users)
                return json.dumps(users)
            except Exception as e:
                print(e)
                return "Error"
    def addRecord(self,id,name):
        try:
            cur = con.cursor()
            cur.execute("insert into users values(?, ?)",(id,name))
            con.commit()
            return "Success"
        except Exception as e:
            print(traceback.format_exc())   
            con.rollback()
            print('Exception in addDummyData')
            return "Failed"   


    
