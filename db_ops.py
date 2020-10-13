# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:27:03 2020

@author: hellf
"""

import cx_Oracle

class db_writer():
    
    def __init__(self,host,sid,port,user,password):
        
        self.host = host
        self.sid = sid
        self.user = user
        self.port = port
        self.password = password

    def db_create_table(self,sql_statement):

        dsn = cx_Oracle.makedsn(self.host,self.port,self.sid)
        connection = cx_Oracle.connect(self.user,self.password, dsn, cx_Oracle.SYSDBA)
        cursor = connection.cursor()
        if sql_statement.startswith('CREATE TABLE'):
            cursor.execute(sql_statement)
        else:
            raise Exception("Is not a Create table operation")
        connection.close()
        
    def db_insert(self,sql_statement):

        dsn = cx_Oracle.makedsn(self.host,self.port,self.sid)
        connection = cx_Oracle.connect(self.user,self.password,dsn, cx_Oracle.SYSDBA)
        cursor = connection.cursor()

        
        cursor.execute(sql_statement)
       
        connection.close()        