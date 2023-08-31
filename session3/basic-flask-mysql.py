import os
#import mysql.connector #pip install mysql-connector-python
#from datetime import date
from functools import wraps
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "mitoken"


#def estudiante_insert(codigo = 0, nombre = ""):
#    hoy = date.today()
#    mydb = mysql.connector.connect(
#        host="",
#        user="",
#        password="",
#        database="",
#        port=0
#    )
#    mycursor = mydb.cursor()
#    sql = "INSERT INTO student (code, name) VALUES (%s, %s)"
#    val = (codigo, nombre)
#    mycursor.execute(sql,val)
#    mydb.commit()
#    return True



def token_required(f):
     @wraps(f)
     def validate(*args, **kwargs):
         client_token = request.headers['token']
         #server_token = app.config['SECRET_KEY']
         server_token = "securetoken"
         if client_token == server_token:
             return f(*args, **kwargs)
         else:
             return jsonify({"message":"token is invalid"}), 403    
     return validate 




@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome class OPEN endpoint"})

@app.route('/estudiante', methods=['GET'])
#@token_required
def estudianteget():
    return jsonify({"Choo Choo": "Retorna informacion del estudiante"})

@app.route('/estudiante', methods=['POST'])
#@token_required
def estudiantepost():
    try:
        return jsonify({"Choo Choo": "Endpoint para insertar estudiante"})
        #estudiante_codigo = request.form['codigo']
        #estudiante_nombre = request.form['nombre']
        #respuesta = estudiante_insert(estudiante_codigo,estudiante_nombre)
        #if(respuesta):
        #    return jsonify({"message":"success"})
    except Exception as e:
        return jsonify({"message":"Error. " + str(e)}), 400 



"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 