import urllib3
from flask import Flask
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
  
def test_nopage_2():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/signin')
    assert 404 == r.status
  
def test_db_update_size():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tops SET Top_Size=(9) WHERE Top_ID = 1")
        mysql.connection.commit() 
        cur.execute("SELECT Top_Size FROM tops WHERE Top_ID = 1")
        mysql.connection.commit()
        x = [row[0] for row in cur.fetchall()]      
        cur.close()
        assert 9 == x[0]

def test_db_update_price():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tops SET Top_Price=('10') WHERE Top_ID = 2")
        mysql.connection.commit() 
        cur.execute("SELECT Top_Price FROM tops WHERE Top_ID = 1")
        mysql.connection.commit()
        x = [row[0] for row in cur.fetchall()]      
        cur.close()
        assert ('10') == x[0]


def test_db_insert():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("INSERT INTO tops (Top_Description, Top_Image,Top_Size, Top_Colour,Top_Price,Wardrobe_ID) VALUES ('Pinkshirt','https://img.ltwebstatic.com/images2_pi/2019/07/03/1562143662675996227_thumbnail_600x799.webp','6','Red','25', '1')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 

def test_db_insert_user():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("INSERT INTO USER (first_name, second_name,username, email,password) VALUES ('Mohammed','Zaheer','MZaheer','mzaheer@gmail.com','hellothere96')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 


def test_db_delete_user():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("DELETE FROM USER WHERE username = ('MZaheer')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 


def test_db_select():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM tops")
        mysql.connection.commit()         
        cur.close()
        assert 7 == num_of_records 

def test_db_select_OR():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM tops WHERE Top_Description = ('Jersey T-shirt   ') OR Top_Colour = ('White')")
        mysql.connection.commit()         
        cur.close()
        assert 2 == num_of_records 


def test_db_select_wardrobe():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM wardrobe")
        mysql.connection.commit()         
        cur.close()
        assert 2 == num_of_records 

def test_db_select_wardrobe_2():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM wardrobe WHERE Wardrobe_Colour = ('White') OR Wardrobe_Description =('Summer')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 

def test_db_select_wardrobe_3():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM wardrobe WHERE Wardrobe_Colour = ('Black') AND Wardrobe_Description =('Summer')")
        mysql.connection.commit()         
        cur.close()
        assert 0 == num_of_records 


def test_db_select_user():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM USER")
        mysql.connection.commit()         
        cur.close()
        assert 2 != num_of_records 


def test_db_select_tops():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tops WHERE Top_Description = ('Jumper')")
        x = [row[2] for row in cur.fetchall()]
        mysql.connection.commit()         
        cur.close()
        assert ('Jumper') == x[0]


def test_db_select_tops_2():
    with app.app_context():
        cur = mysql.connection.cursor()
        x = cur.execute("SELECT * FROM tops WHERE Top_Description = ('Raglan Sleeve Jumper') AND Top_Colour = ('White')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == x

def test_db_delete():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("DELETE FROM tops WHERE Top_Description = ('Pinkshirt')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == num_of_records 

def test_db_select_SUM():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT SUM(Top_Price) FROM tops")
        mysql.connection.commit()
        x = [row[0] for row in cur.fetchall()]      
        cur.close()
        assert (110.0) == x[0]

def test_db_greater_equal():
    with app.app_context():
        cur = mysql.connection.cursor()
        num_of_records = cur.execute("SELECT * FROM tops WHERE Top_Price >= ('25')")
        mysql.connection.commit()         
        cur.close()
        assert 2 == num_of_records 


def test_db_login():
    with app.app_context():
        cur = mysql.connection.cursor()
        username = cur.execute("SELECT * FROM USER WHERE username  = ('HifzaZaheer96')")
        mysql.connection.commit()         
        cur.close()
        assert 1 == username 

def test_db_login_email():
    with app.app_context():
        cur = mysql.connection.cursor()
        email = cur.execute("SELECT * FROM USER WHERE email  = ('hifza@yahoo.com')")
        mysql.connection.commit()         
        cur.close()
        assert 0 == email 


def test_avg_price():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT AVG(Top_Price)FROM tops")
        x = [row[0] for row in cur.fetchall()]
        mysql.connection.commit()         
        cur.close()
        assert 18.333333333333332 == x[0]


def test_minimum_size():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT MIN(Top_Size)FROM tops")
        x = [row[0] for row in cur.fetchall()]
        mysql.connection.commit()         
        cur.close()
        assert 6 == x[0]

def test_maximum_size():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT MAX(Top_Size)FROM tops")
        x = [row[0] for row in cur.fetchall()]
        mysql.connection.commit()         
        cur.close()
        assert 12 == x[0]

def test_distinct_top_colour():
    with app.app_context():
        cur = mysql.connection.cursor()
        x = cur.execute("SELECT DISTINCT Top_Colour FROM tops")
        mysql.connection.commit()         
        cur.close()
        assert 5 == x

def test_distinct2():
    with app.app_context():
        cur = mysql.connection.cursor()
        x = cur.execute("SELECT DISTINCT Top_Price FROM tops")
        mysql.connection.commit()         
        cur.close()
        assert 5 == x

def test_between_price():
    with app.app_context():
        cur = mysql.connection.cursor()
        x = cur.execute("SELECT * FROM tops WHERE Top_Price BETWEEN 10 AND 25;")
        mysql.connection.commit()         
        cur.close()
        assert 5 == x
        
def test_between_price2():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(Top_Price) FROM tops WHERE Top_Price BETWEEN 10 AND 20;")
        mysql.connection.commit()  
        x = [row[0] for row in cur.fetchall()]      
        cur.close()
        assert 4 == x[0]