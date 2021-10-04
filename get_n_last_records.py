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

result = cursor.execute(f'''SELECT * FROM plants ORDER BY plant_id DESC LIMIT {id}''')

data = cursor.fetchall()

print (f'''\nID:  Name:         description:       number:  price: rare:''')
for i in data:
    print ('',str(i[0]).ljust(4),  i[1].ljust(14),    i[2].ljust(20),   str(i[3]).ljust(6), str(i[4]).ljust(7), i[5])

cursor.close()
print()


