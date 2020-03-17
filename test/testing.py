import urllib3
from flask import Flask,render_template, request,redirect,url_for,flash, session
from flask_mysqldb import MySQL
import os


app = Flask(__name__)



app.config["MYSQL_HOST"] = os.environ['MYSQL']
app.config["MYSQL_USER"] = os.environ['USER']
app.config["MYSQL_PASSWORD"] = os.environ['PASSWORD']
app.config["MYSQL_DB"] = os.environ['DATABASE']

mysql = MySQL(app)

def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/')
    assert 200 == r.status

def test_aboutpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/about')
    assert 200 == r.status

def test_shopsummerclothespage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/shopclothes')
    assert 200 == r.status

def test_shopwinterclothespage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/shopclotheswinter')
    assert 200 == r.status

def test_contactpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/contact')
    assert 200 == r.status

def test_registerpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/register/')
    assert 200 == r.status

def test_loginpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/login/')
    assert 200 == r.status

def test_crudpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/crud')
    assert 200 == r.status
  
def test_nopage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/crudoperation')
    assert 404 == r.status
  
def test_db():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("Select * from tops")                                  #this and next command will get records before update
        records_before = cur.fetchall()
        cur.execute("INSERT INTO tops (Top_Description, Top_Image,Top_Size, Top_Colour,Top_Price,Wardrobe_ID) VALUES ('Pinkshirt','https://img.ltwebstatic.com/images2_pi/2019/07/03/1562143662675996227_thumbnail_600x799.webp','6','Red','25', '1')")
        mysql.connection.commit()
        cur.execute("Select * from tops")                                           #this gets record after update
        records_after = cur.fetchall()          
        cur.close()
    recordb = len(records_before)                                                        #finds length of records before change
    new_id = records_before[recordb-1][0]+1                                                      #finds the id of the previous record and + 1 for autoincrement new rec
    recorda = len(records_after) 
    assert (new_id,'https://img.ltwebstatic.com/images2_pi/2019/07/03/1562143662675996227_thumbnail_600x799.webp','Pinkshirt',6,'Red','25', 1) == records_after[recorda-1]                           #compares what should be there to most recent record