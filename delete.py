from flask import Flask
from flaskext.mysql import MySQL
from sys import argv

id = argv[1]

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'mr-robot'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dfcdewq1'
app.config['MYSQL_DATABASE_DB'] = 'orangery'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


conn = mysql.connect()
cursor =conn.cursor()

cursor.execute(f'''DELETE FROM plants WHERE plant_id={id}''')

conn.commit()


cursor.close()
print(' Done ! ...')

