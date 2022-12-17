import mysql.connector

def getconnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="air_quality"
    )
    mycursor = mydb.cursor()
    if (not mydb or not mycursor):
        raise ValueError('DB is not connected')
    
    return mydb, mycursor

def dbinsertmonitoring(value):
    mydb, mycursor = getconnection()
    if (not mydb or not mycursor):
        raise ValueError('DB is not connected')
    sql = "INSERT INTO monitoring (data) VALUES (%s)"
    param = ([value])
    mycursor.execute(sql, param)

    mydb.commit()

def dbfetchlatestdata():
    mydb, mycursor = getconnection()
    if (not mydb or not mycursor):
        raise ValueError('DB is not connected')
    mycursor.execute("SELECT * FROM monitoring ORDER BY created_date DESC LIMIT 1")
    myresult = mycursor.fetchone()
    return myresult