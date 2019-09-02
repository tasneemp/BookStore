# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:37:13 2019

@author: Tasneem
"""

import sqlite3

class Database:
    
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS BOOK(ID INTEGER PRIMARY KEY,TITLE TEXT,AUTHOR TEXT,YEAR INTEGER,ISBN INTEGER) ")
        
    def insert(self,title,author,year,isbn):
        
        self.cur.execute("INSERT INTO BOOK VALUES(NULL,?,?,?,?) " ,(title,author,year,isbn))
        self.conn.commit()
        
     
    def view(self):
        
        self.cur.execute("SELECT * FROM BOOK")
        output=self.cur.fetchall()
        return output
    
    def search(self,title='',author='',year='',isbn=''):
        self.cur.execute("SELECT * FROM BOOK WHERE TITLE=? OR AUTHOR = ? OR YEAR=? OR ISBN=?",(title,author,year,isbn))
        output=self.cur.fetchall()
        return output
        
    def delete(self,id):
        self.cur.execute("DELETE FROM BOOK WHERE ID=?" ,(id,))
        self.conn.commit()
        
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE BOOK SET TITLE=?,AUTHOR=?, YEAR=?, ISBN=? WHERE ID=?" ,(title,author,year,isbn,id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()        

