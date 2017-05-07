# pyPostgres-connector

Module to connect to a postgres database...

```python
#Initialize class:
x = db_connect(username, password, url_to_server, database_name)

#Make a query on the database
df = x.conn.query("""
		  ENTER THE 
		  QUERY HERE!!
	  """)
df is returned as a pandas dataframe
```
