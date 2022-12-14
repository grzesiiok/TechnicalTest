import mysql.connector
import applybonus
import display
import import2csv

con = mysql.connector.connect(user ='root', password= 'p', host = '127.0.0.1',port='3306', database='coindb')


def check_employee(employee_id):
    #sql search
    sql = 'select * from empd where id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount

    if r == 1:
        return True
    else:
        return False

def check_deparatment(departament_id):
    #sql search
    sql = 'select * from dep where id=%s'
    c = con.cursor(buffered=True)
    data = (departament_id,)
    c.execute(sql, data)
    r = c.rowcount

    if r == 1:
        return True
    else:
        return False

def Add_Employ():
    Id = input("Enter Employee Id : ")


    if (check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()

    else:
        first_Name = input("Enter Employee First Name : ")
        last_Name = input("Enter Employee Last Name : ")
        age = input("Enter Employee Age : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        bonus = input("Enter Employee Bonus : ")
        total = applybonus.bonus(Salary,bonus)
        data = (Id, first_Name, last_Name, age, Post, Salary, bonus, total)

        sql = 'insert into empd values(%s,%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()

        c.execute(sql, data)

        con.commit()
        print("Employee Added Successfully ")
        menu()

#adding departament
def design():
    Id = input("Enter Departament Id : ")

    if (check_deparatment(Id) == True):
        print("Departament aready exists\nTry Again\n")
        menu()

    else:
        Name = input("Enter Employee First Name : ")
        users = input("Enter Users : ")
        data = (Id, Name, users)
        sql = 'insert into dep values(%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)

        con.commit()
        print("Employee Added Successfully ")
        menu()

#adding employee to departament
def adding_emp2dep():
    Id = input("Enter Employee Id : ")

    if (check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()

    else:
        c = con.cursor()
        c.execute('''INSERT INTO dep
        SELECT Id, User_Name FROM empd
        WHERE id = %s''',(Id))
        con.commit()
        print("Employee Added Successfully ")
        menu()

#deleting employee to departament
def del_emp2dep():
    Id = input("Enter Employee Id : ")

    if (check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()

    else:
        c = con.cursor()
        c.execute('''DELETE FROM empd WHERE Id = %s''',(Id))
        con.commit()
        print("Employee Added Successfully ")
        menu()

def Promote_Employee():
    Id = int(input("Enter Employ's Id"))

    if (check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))

        sql = 'select total from empd where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        r = c.fetchone()
        t = applybonus(Amount,r[0])

        sql = 'update empd set total=%s where id=%s'
        d = (t, Id)
        c.execute(sql, d)
        con.commit()

        ######
        sql = 'select bonus from empd where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        sql = 'update empd set total=%s where id=%s'
        d = (Amount, Id)
        c.execute(sql, d)
        con.commit()


        print("Employee Promoted")
        menu()


def Remove_Employ():
    Id = input("Enter Employee Id : ")

    if (check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:

        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        con.commit()
        print("Employee Removed")
        menu()


def check_employee(employee_id):

    sql = 'select * from empd where id=%s'

    c = con.cursor(buffered=True)
    data = (employee_id,)

    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


def Display_Employees():

    sql = 'select * from empd'
    c = con.cursor()
    c.execute(sql)

    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee First Name : ", i[1])
        print("Employee Last Name : ", i[2])
        print("Employee Age : ", i[3])
        print("Employee Post : ", i[4])
        print("Employee Salary : ", i[5])
        print("Employee Bonus : ", i[6])
        print("Employee Total : ", i[7])

    menu()

def Display_Employee():
    employee = input('Employee name:')
    c = con.cursor()
    c.execute('select * from empd Where Last_Name=%s',(employee,))

    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee First Name : ", i[1])
        print("Employee Last Name : ", i[2])
        print("Employee Age : ", i[3])
        print("Employee Post : ", i[4])
        print("Employee Salary : ", i[5])
        print("Employee Bonus : ", i[6])
        print("Employee Total : ", i[7])

    menu()

def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Display Employee")
    print("6 to Display Departaments")
    print("7 to Display Departaments Employees")
    print("8 to Add Employee to Departament")
    print("9 to Delete Employee from Departament")
    print("10 to Export employer invoice to csv file")
    print("11 to Exit")

    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        Display_Employee()
    elif ch == 6:
        display.deparatments()
    elif ch == 7:
        display.employers()
    elif ch == 8:
        adding_emp2dep()
    elif ch == 9:
        del_emp2dep()
    elif ch == 11:
        import2csv.tocsv()
    elif ch == 10:
        exit(0)
    else:
        print("Invalid Choice")
        menu()

menu()