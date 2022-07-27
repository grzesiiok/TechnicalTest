import mysql.connector
con = mysql.connector.connect(user ='root', password= 'p', host = '127.0.0.1',port='3306', database='coindb')
def employers():
    sql = 'select * from dep'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()

    for i in r:
        print("Departament Id : ", i[0])
        print("Employee of Departament : ", i[2])

def deparatments():
    sql = 'select * from dep'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Departament Id : ", i[0])
        print("Departament Name : ", i[1])