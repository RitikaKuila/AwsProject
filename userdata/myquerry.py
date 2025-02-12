
import mysql.connector


def connection():
	return mysql.connector.connect(

		host='localhost',
		user='root',
		password='',
		database='userdata2',
		)


def insertuserdata(n,e,p):

	con=connection()
	cursor=con.cursor()

	qry='insert into mytable(name,email,phone) values(%s,%s,%s)'
	value=(n,e,p)

	cursor.execute(qry,value)
	con.commit()

	cursor.close()
	con.close()

def fetchuserdata():
	con=connection()
	cursor=con.cursor()
	qry='select * from mytable'

	cursor.execute(qry)
	data=cursor.fetchall()

	cursor.close()
	con.close()
	return data

def fetchuser_details(id):
	con=connection()
	cursor=con.cursor()
	qry='select * from mytable where id='+str(id)

	cursor.execute(qry)
	data=cursor.fetchall()

	cursor.close()
	con.close()
	return data

def updateuserdata(n,e,p,id):

	con=connection()
	cursor=con.cursor()

	qry='update mytable set name=%s,email=%s,phone=%s where id=%s'
	value=(n,e,p,id)

	cursor.execute(qry,value)
	con.commit()

	cursor.close()
	con.close()

def deluserdata(id):
	con=connection()
	cursor=con.cursor()

	qry='delete from mytable where id='+str(id)
	cursor.execute(qry)
	con.commit()

	cursor.close()
	con.close()
