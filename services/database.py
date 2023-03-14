import pyodbc

server = '022621-GTI\SQLEXPRESS' 
database = 'controle_financeiro_python' 
username = 'sa' 
password = 'Onl3023@#'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()