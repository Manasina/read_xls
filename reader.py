import pyexcel
import cx_Oracle
import warn
records = pyexcel.iget_records(file_name="real.xlsx")
connection = cx_Oracle.connect(user="hr", password="welcome",
                               dsn="localhost/orclpdb1")
cursor = connection.cursor()
for donnes in records:
    value = [str(value).replace(';', '') for key, value in donnes.items()]
    keys = [str(key).replace(';', '') for key, value in donnes.items()]
    cursor.execute((f"""
         INSERT INTO Customers ({', '.join(keys)})
 VALUES ({', '.join(value) });"""))
