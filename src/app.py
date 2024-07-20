from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'operadores'

mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connection
    cursor = conn.cursor()

    sql = "insert into operadores (id, apellido, nombre, jerarquia, legajo, dni, telefono, foto) values (null,'Rios', 'Juan', 'suboficial', 700523, 40451236, '3413578963', 'fotoRJuan.jpg');"

    cursor.execute(sql)
    conn.commit()

    return render_template('operadores/index.html')

if __name__ == '__main__':
    app.run(debug=True)