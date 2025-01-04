import mysql.connector #importing module

mydb=mysql.connector.connect(host="localhost", user="root", password="", database="practicals2", charset="utf8")
#connected to mysql
mycursor=mydb.cursor()#connecting to mysql cursor

mycursor.execute("Create table register(indexNo int,class int,topic varchar(20),status varchar(8));")
#creating table

for i in range(0,5):  
    ent1=int(input("Enter indexno."))
    ent2=int(input("Enter class"))
    ent3=input("Enter Topic")
    ent4=input("Enter Status")
    val="Insert into register values('%d','%d','%s','%s');"%(ent1,ent2,ent3,ent4)
    mycursor.execute(val)  #string formatting for values
    
mycursor.execute("select * from register;") #displaying register details
records=mycursor.fetchall()
for x in records:
    print(x)
    
mycursor.execute("Select * from register where topic like 'P%';")
rec=mycursor.fetchall()            #displaying register details where topic starts with s
for y in rec:
    print(y)
    
mydb.commit()