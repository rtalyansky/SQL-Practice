import sqlite3 

def try_fetchone(cursor):
	count = 0
	while (True):
		r = cursor.fetchone()
		if r == None:
			break
		else:
			count += 1
			print ("Row %d:" % count), r


#def try_fetchmany(cursor, howmany):
#	iteration = 0
#	while(True):
#		l = cursor.fetchmany(howmany)
#		if l == []:
#			break
#		else:
#			iteration += 1
#			print "Iteration", iteration
#			for r in l:
#				print r

dbconn = sqlite3.connect ('Northwind.db') 

dbconn.text_factory = bytes

cursor = dbconn.cursor()

sql = "select city from customers" 

cursor.execute(sql)
try_fetchone(cursor)

#cursor.execute(sql)
#try_fetchmany(cursor, 4)

cursor.close()
dbconn.close()