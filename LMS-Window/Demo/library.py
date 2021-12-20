import sqlite3
DATABASE_NAME='library.db'
def createUsersTable():
    con=sqlite3.connect(DATABASE_NAME,check_same_thread=False)
    cur=con.cursor()
    cur.execute('create table if not exists users(id integer primary key autoincrement,name text,role text,email text,password text)')
    con.commit()

def getUsers():
    con=sqlite3.connect(DATABASE_NAME,check_same_thread=False)
    cur=con.cursor()
    cur.execute('select * from users')
    rows=cur.fetchall() #POSTGRESQL
    return rows

def addUser(name,email,password,role):
    con=sqlite3.connect(DATABASE_NAME,check_same_thread=False)
    cur=con.cursor()
    cur.execute('insert into users(name,email,password,role) values(?,?,?,?)',(name,email,password,role))
    con.commit()   

def loginUser(email,password):
    con=sqlite3.connect(DATABASE_NAME,check_same_thread=False)
    cur=con.cursor()
    cur.execute('select * from users where email=? and password=?',(email,password))
    rows=cur.fetchone()
    print(rows)
    return rows    




createUsersTable()


