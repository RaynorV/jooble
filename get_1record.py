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

result = cursor.execute(f'''SELECT * FROM plants WHERE plant_id={id}''')

data = cursor.fetchone()

print (f'''\nID:  Name:         description:       number:  price: rare:''')
print (' '+str(data[0]).ljust(4),  data[1].ljust(14),    data[2].ljust(20),   str(data[3]).ljust(6), str(data[4]).ljust(7), data[5])

cursor.close()
print()

