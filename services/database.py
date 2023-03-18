import pyodbc

server = 'HfdfdSS' 
database = 'controle_financeiro_python' 
username = 'sa' 
password = '30dfdfd00'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()