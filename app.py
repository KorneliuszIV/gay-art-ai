from flask import Flask, render_template, request, redirect, session, url_for, g, send_from_directory
from flask_session import Session
import dotenv 
from database import get_db, close_db
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)
app.config["SECRET_KEY"] = "whatevr"
app.config["SESSION_PERNAMENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

submitted_ips = set()
def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers["X-Forwarded-For"].split(",")[0].strip()
    return request.remote_addr



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        user_ip = get_client_ip()
        submitted_ips.add(user_ip)
        if user_ip in submitted_ips:
            return "You have already submitted a rating!", 403
        print(submitted_ips)
        return render_template('index.html')
    x1 = request.form.get('art1')
    x2 = request.form.get('art2')
    x3 = request.form.get('art3')
    x4 = request.form.get('art4')
    x5 = request.form.get('art5')
    x6 = request.form.get('art6')
    x7 = request.form.get('art7')
    x8 = request.form.get('art8')
    x9 = request.form.get('art9')
    x10 = request.form.get('art10')
    sex = request.form.get('sex')
    
    data_str = x1+ x2+x3+x4+x5+x6+x7+x8+x9+x10+sex
    print(data_str)
    with open('graph_data.txt', 'w') as file:
        file.write(data_str)
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO data (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,y) 
                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', 
                  (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,sex))
    db.commit()
    cursor.close()
    return render_template('response.html')




@app.route("/level_data")
def level_data():
    return send_from_directory('.', 'graph_data.txt')

if __name__ == "__main__":
    app.run()