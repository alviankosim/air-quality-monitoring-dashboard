import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="air_quality"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM monitoring LIMIT 10")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)