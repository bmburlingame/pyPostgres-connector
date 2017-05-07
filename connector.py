"""
------------------------
Shyft Technologies Inc.
Shyft - Apr 2017
------------------------
Module to connect to Shyft databases.

-Bryan Burlingame
"""

import psycopg2
import pandas as pd
import numpy as np
import os

class db_connect():
    """Class to connect to Shyft Databases"""

    def __init__(self, username, password, url, database):
        """Init"""

        #Define Variables
        self.__username__ = username
        self.__password__ = password
        self.__server__ = url
        self.__database__ = database

        #Connect to database
        self.conn = self.__connect__()



    def __connect__(self):
        """Connect to Shyft database"""
        try:
            conn = psycopg2.connect(dbname = self.__database__,
                                    user = self.__username__,
                                    password = self.__password__,
                                    host = self.__server__
                                    )
            print "Your are connected to " + self.__database__ + " on the " + \
                    self.__server__ + " server!"
            return conn
        except:
            print "I am unable to connect to the database"


    def query(self, query):
        """Queries Database
           Pass in Query as a String"""
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        rows = pd.DataFrame(rows)
        return rows


