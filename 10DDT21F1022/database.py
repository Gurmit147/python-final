import mysql.connector
#create connection
mydb = mysql.connector.connect(
	user="root",
	host="localhost",
	password="",
	database="LelemoveSystem")
#create cursor

mycursor = mydb.cursor()

#create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS LelemoveSystem")

table = """CREATE TABLE IF NOT EXISTS package(
Item_id VARCHAR(10) PRIMARY KEY NOT NULL ,
Item_height VARCHAR(5),
Item_width VARCHAR(5),
Item_length VARCHAR(5),
Item_volume VARCHAR(10),
Item_price VARCHAR(5))"""

mycursor.execute(table)



