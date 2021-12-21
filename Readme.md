
#JSON: Java script object notation

1. Front-end developer 
2. Backend developer 

Data exchange Formats:
1. JSON
2. XMl
3. Protobuf

JSON: JSONOBject, Json Array

[
{
   "full_name":"Ramesh",
   "age": 30,
   "address":{
       "village":"Vizag",
       "state":"AP",
       "pincode":500012
   },
   "mobile":    
},
{
   "full_name":"Laxman",
   "age": 30 
}
]



datetime: Obj to string -> Date Formating 
date string ->date -> Date Parse 



#Library Management System

User module: 
1. User login
   1. Librarian Login (Admin)
   2. Student Login

Books Module:
1.Add books
2.View Books
3.Update Books
4.Delete Books

(id,title,author,description)


Students Module:
1.Add Student
2.View Students
3.Update Students
4.Delete Students
(id,name,rollno,class,branch,role) role=student|admin

id:100 (admin)
id:200 (student)


Book Issue :
1.Assign a book to Student
2.Return a Book to Library


#DATE TIME (SQLITE)
CREATE table dt(issue text)

INSERT into dt(issue) values(datetime('now', 'localtime'))

SELECT * from dt

SELECT	date(issue),	time(issue) FROM	dt;

SELECT * FROM dt WHERE    strftime('%s',issue) BETWEEN strftime('%s', '2021-12-12') AND strftime('%s', '2021-12-30')

SELECT * FROM dt WHERE    strftime('%s',issue) > strftime('%s', '2021-12-15')


-------- 
Backend + Front End (Fullstack)

Backend: Create Database and provide the data in the form of JSON/XML
Frontend: Consume Rest APIs and disply it on Website/Mobile App/Desktop app

Project:
1. Requirement (Software Requiremnt Specifications) : 
2. Analysis : Define Features
3. Design (proto type) : Wireframes ->Client Feedback-> Changes   
4. Developemnt
5. Testing  
6. Deployment(Production)

-----
LMS:
1. Users: (Staff/Students)
2. Books
3. Issue Book: (Request Issue/Issue Book/Return Book)



 