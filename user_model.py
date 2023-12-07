import mysql.connector
from flask import jsonify
class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost" , user = "root" , password="" , database = "MY_DB" )
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)    
        except:
            print("error")        

    def user_getall(self):
        self.cur.execute("SELECT * FROM Library")
        res  = self.cur.fetchall()
        if len(res)>0:
            return jsonify(res)
        else:
            return "NO DATA FOUND "

    def user_addone(self,data):
        if 'name' in data and 'body' in data:
            self.cur.execute(f"INSERT INTO Library(name, body) VALUES('{data['name']}' , '{data['body']}')")
            return "NEW BOOK ADDED"
        else:
            return "ERROR: NAME AND BODY VALUES CANT BE EMPTY"
    
    def user_update(self,id ,data):
        if 'name' in data and 'body' in data:
            self.cur.execute(f"UPDATE Library SET name='{data['name']}' , body = '{data['body']}' WHERE id= {id}")
            if self.cur.rowcount>0:
                return "UPDATE SUCESSFUL"
            else:
                return "UPDATE FAILED"
        else:
            return "ERROR: NAME AND BODY VALUES CANT BE EMPTY"