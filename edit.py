from flask import Flask
from flaskext.mysql import MySQL
from sys import argv

id = argv[1]
name = str(argv[2])
desc = str(argv[3])
number = int(argv[4])
price = int(argv[5])
rare = str(argv[6])

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'mr-robot'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dfcdewq1'
app.config['MYSQL_DATABASE_DB'] = 'orangery'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


conn = mysql.connect()
cursor =conn.cursor()

cursor.execute(f'''UPDATE plants SET name='{name}', description='{desc}', number={number}, price={price}, rare='{rare}' WHERE plant_id={id}''')

conn.commit()

cursor.close()
print(' Done ! ...')

