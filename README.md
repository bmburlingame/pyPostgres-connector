# pyPostgres-connector

Module to connect to a postgres database...

Initialize class:
x = db_connect(username, password, url_to_server, database_name)

df = x.query("""
		  ENTER THE 
		  QUERY HERE!!
	  """)
df is returned as a pandas dataframe

