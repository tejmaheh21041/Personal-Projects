import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='Priyanshu',charset="utf8")
mycur=mydb.cursor()
#mycur.execute("Insert into student values(24,'Priyanshu',17,12,4891);")
mycur.execute("select * from student;")
print(mycur.fetchall())