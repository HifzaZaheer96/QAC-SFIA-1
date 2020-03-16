from flask import Flask,render_template, request,redirect,url_for,flash, session
from flask_mysqldb import MySQL
import os
import variables
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)



app.config["MYSQL_HOST"] = os.environ['MYSQL']
app.config["MYSQL_USER"] = os.environ['USER']
app.config["MYSQL_PASSWORD"] = os.environ['PASSWORD']
app.config["MYSQL_DB"] = os.environ['DATABASE']

mysql = MySQL(app)
variabless = variables
app.config['SECRET_KEY'] = 'secret'

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
        return render_template("index.html" , title="Home", info1=info)

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
            for i in range(0,len(info)) :
                if Top_Description == info[i][2]:
                    variabless.delete = "Successfully Deleted Top details!!"
                    return redirect (url_for('crud'))
                else:
                    variabless.delete = "Sorry!! Please enter matching Top Description!"
            return redirect (url_for('crud'))


            # for i in info[2] :
            #     if Top_Description == i:
            #         return render_template("index.html", title="Home", info1=info)
            #     return redirect (url_for('home'))
            # return render_template("index.html", title="Home", info1=info,messagesuccess = "Successfully deleted the information")


@app.route('/about')
def about():
    return render_template("about.html", title='About Us')

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
    return render_template("shopclothes.html", info1=info,title="Summer Clothes")
    


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
    return render_template("shopclotheswinter.html", info1=info,title="Winter Clothes")



@app.route('/contact')
def contact():
    return render_template("contact.html", title='About Us')

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
                    variabless.message = "Successfully updated Top details!!"
                    return redirect (url_for('crud'))
                else:
                    variabless.message = "Sorry!! Please enter matching Top Description!"
            return redirect (url_for('crud'))
            
            


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userDetails = request.form
        if userDetails['password'] != userDetails['confirm_password']:
            flash('Password do not match! Try again.', 'danger')
            return render_template('register.html')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO USER(first_name, second_name, username, email, password) VALUES (%s,%s,%s,%s,%s)", (userDetails['first_name'], userDetails['second_name'], userDetails['username'], userDetails['email'], generate_password_hash(userDetails['password'])))
        mysql.connection.commit()
        cur.close()
        flash('Registeration successful! Please login.', 'success')
        return redirect('/login/')
    return render_template('register.html',title="Register")


@app.route('/crud', methods=['GET', 'POST'])
def crud():
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
        Top_Image=details['tpic']
        Top_Description=details['tname']
        Top_Size=details['tsize']
        Top_Colour=details['tc']
        Top_Price=details['tp']
        WARDROBE_ID = details['wid']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tops (Top_Image,Top_Description, Top_Size, Top_Colour,Top_Price,WARDROBE_ID) VALUES (%s,%s, %s, %s ,%s,%s)", (Top_Image,Top_Description, Top_Size, Top_Colour,Top_Price,WARDROBE_ID))
        mysql.connection.commit()
        cur.close()
        return redirect (url_for('crud'))

    return render_template('crud.html',info1=info, title="CRUD", message= variabless.message, delete = variabless.delete)


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM USER WHERE username = %s", ([username]))
        print(resultValue)
        if resultValue > 0:
            user = cur.fetchone()
            print(user)
            l = []
            for i in user:
                    l.append(i)
                    print(l)
            if check_password_hash(l[5], userDetails['password']):
                session['login'] = True
                mysql.connection.commit()
            else:
                print("second else")
                cur.close()
                return render_template('login.html', message="Password does not match")
        else:
            cur.close()
            return render_template('login.html', message='username not found')
        cur.close()
        flash("You've successfully logged in!", 'success')
        return redirect('/crud')
    return render_template('login.html',title="Login")



@app.route('/logout')
def logout():
    session['login'] = False
    flash("You have been logged out!", 'info')
    return redirect('/login/')



if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)


#   return redirect(url_for('index'))
#     return render_template('add.html', form = form)
