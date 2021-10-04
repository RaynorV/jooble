from flask import Flask
from flaskext.mysql import MySQL
from sys import argv

name = str(argv[1])
desc = str(argv[2])
number = int(argv[3])
price = int(argv[4])
rare = str(argv[5])

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'mr-robot'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dfcdewq1'
app.config['MYSQL_DATABASE_DB'] = 'orangery'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


conn = mysql.connect()
cursor =conn.cursor()

cursor.execute(f'''INSERT INTO plants (plant_id, name, description, number, price, rare)  VALUES(NULL, '{name}', '{desc}', '{number}', '{price}', '{rare}')''')

conn.commit()

cursor.close()
print(' Done ! ...')

