from flask import Flask
from threading import Thread
import mysql.connector
import os
import random
from dotenv import load_dotenv
import json

load_dotenv(dotenv_path="config")


mydb = mysql.connector.connect(
     host=os.getenv("HOST"),
     user=os.getenv("USER"),
     database=os.getenv("DATABASE"),
     port=os.getenv("PORT"),
     password=os.getenv("PASS")
               )

app = Flask('')

@app.route("/")
def home():
    #print(mydb)
    return "Im alive"

@app.route("/test")
def test():
    #print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT msg FROM touser ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchall()
    return json.dumps(random.choice(myresult)[0])


def run():
    app.run(host='0.0.0.0',port=9000)

def keep_alive():
    t = Thread(target=run)
    t.start()
