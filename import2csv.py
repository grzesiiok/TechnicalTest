import pyodbc
import pandas as pd

conn = pyodbc.connector.connect(user ='root', password= 'p', host = '127.0.0.1',port='3306', database='coindb')

def tocsv():
    Id = input("Enter Employee Id : ")

    employee = input('Employee name:')
    sql_query = pd.read_sql_query('''select * from empd Where Id=%s''',Id, conn)
    df = pd.DataFrame(sql_query)
    df.to_csv (r'C:\Users\Ron\Desktop\exported_data.csv', index = False)