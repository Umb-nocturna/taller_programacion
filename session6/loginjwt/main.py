from flask import Flask, request, jsonify, make_response, request, render_template, session, flash #pip install Flask
import mysql.connector # pip install mysql-connector-python
import os
import jwt # pip install PyJWT
from datetime import datetime, timedelta
from functools import wraps
import time
import pytz


app = Flask(__name__)


app.config['SECRET_KEY'] = '1234567890'


def token_required(func):
    """decorator factory which invoks update_wrapper()"""
    @wraps(func)
    def decorated(*args, **kwargs):
        headers = request.headers
        bearer = headers.get('Authorization')    
        token = bearer.split()[1]
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except Exception as e:
            return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return decorated

def get_all_heroes():
    """Function return all heroes from mysql."""
    mydb = mysql.connector.connect(
        host="containers-us-west-101.railway.app",
        user="root",
        password="6G74WClR1fVadVdFKqFX",
        database="railway",
        port=7171
    )
    cursor = mydb.cursor()
    cursor.callproc('sp_list_avengers')
    for result in cursor.stored_results():
        heroes = result.fetchall()
    
    json_heroes = json.dumps(heroes)
    return json_heroes
        
#1.Endpoint Default
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'logged in currently'

#2.Endpoint public
@app.route('/public')
def public():
    return 'For Public'

#3.Endpoint private
@app.route('/auth')
@token_required
def auth():
    return jsonify({'status':"ok","msg":"Acceso a la informacion protegida o privada"})

#4.Endpoint get token
@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        utc_bogota = datetime.now(pytz.timezone('America/Bogota'))
        timestamp = datetime.timestamp(utc_bogota)
        token = jwt.encode({
            'user': request.form['username'],
            'expiration': int(timestamp)
        },
            app.config['SECRET_KEY'])
        return jsonify({'jwt': token})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})
        
    
"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000)) 