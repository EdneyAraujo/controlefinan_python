import pyodbc

server = 'HOdSERfSTsPRESS' 
database = 'controle_financeiro_python' 
username = 'sa' 
password = '3d0232v'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()