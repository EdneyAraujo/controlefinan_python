import pyodbc

server = '0224\SQLEXPRESS' 
database = 'controle_financeiro_python' 
username = 'sa' 
password = '12233'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()