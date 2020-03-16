from flask import Flask,render_template, request,redirect,url_for
from flask_mysqldb import MySQL
import os
import variables
app = Flask(__name__)


app.config["MYSQL_HOST"] = os.environ['MYSQL']
app.config["MYSQL_USER"] = os.environ['USER']
app.config["MYSQL_PASSWORD"] = os.environ['PASSWORD']
app.config["MYSQL_DB"] = os.environ['DATABASE']

mysql = MySQL(app)

variabless = variables


@app.route('/' , methods=['GET', 'POST'])
def home():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tops")
        mysql.connection.commit()
        rows = cur.fetchall()
        cur.close()

        info = []

        for row in rows:
            info.append(row)
        print(info)
    
        #return render_template("index.html" , title="Home", info1=info)

   

        if request.method == "POST":   
        
            details=request.form
            Top_Image=details['tpic']
            Top_Description=details['tname']
            Top_Size=details['tsize']
            Top_Colour=details['tc']
            WARDROBE_ID = details['wid']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO tops (Top_Image,Top_Description, Top_Size, Top_Colour,WARDROBE_ID) VALUES (%s,%s, %s, %s ,%s)", (Top_Image,Top_Description, Top_Size, Top_Colour,WARDROBE_ID))
            mysql.connection.commit()
            cur.close()
            return redirect (url_for('home'))
        return render_template("index.html" , title="Homee", info1=info, message= variabless.message, delete = variabless.delete)
        #return redirect(url_for('home'))

@app.route('/tops/delete' , methods=['GET', 'POST'])
def account_delete():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tops")
        mysql.connection.commit()
        rows = cur.fetchall()
        cur.close()

        info = []

        for row in rows:
            info.append(row)    

        if request.method == "POST": 
            details=request.form
            Top_Description=details['tname']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM tops WHERE Top_Description = (%s)",[Top_Description])
            mysql.connection.commit()
            cur.close()
            print("I am printing this out")
            print(Top_Description)
            for i in range(0,len(info)) :
                print(info[i][2])
                if Top_Description == info[i][2]:
                    variabless.delete = "Success"
                    return redirect (url_for('home'))
                else:
                    variabless.delete = "Failure"
            return redirect (url_for('home'))


            # for i in info[2] :
            #     if Top_Description == i:
            #         return render_template("index.html", title="Home", info1=info)
            #     return redirect (url_for('home'))
            # return render_template("index.html", title="Home", info1=info,messagesuccess = "Successfully deleted the information")

@app.route('/shopclothes', methods=['GET','POST'])
def shopclothes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tops WHERE Wardrobe_ID=1")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)
    print(info)
    return render_template("shopclothes.html", info1=info)
    


@app.route('/shopclotheswinter', methods=['GET','POST'])
def shopclotheswinter():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tops WHERE Wardrobe_ID=2")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)
    print(info)
    return render_template("shopclotheswinter.html", info1=info)


@app.route('/tops/update', methods=['GET', 'POST'])
def account_update():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tops")
        mysql.connection.commit()
        rows = cur.fetchall()
        cur.close()
        
        info = []

        for row in rows:
            info.append(row)
        print(info)


        if request.method == "POST": 
            details=request.form
            Top_Description=details['tname']
            Top_Size=details['tsize']
            cur = mysql.connection.cursor()
            cur.execute("UPDATE tops SET Top_Size=(%s) WHERE Top_Description = (%s)",[int(Top_Size), Top_Description])
            mysql.connection.commit()
            cur.close()
            for i in range(0,len(info)) :
                if Top_Description == info[i][2]:
                    variabless.message = "Success"
                    return redirect (url_for('home'))
                else:
                    variabless.message = "Failure"
            return redirect (url_for('home'))
            

            


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)


#   return redirect(url_for('index'))
#     return render_template('add.html', form = form)
