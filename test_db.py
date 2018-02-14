import MySQLdb

db = MySQLdb.connect(host='localhost', user='user',
                     passwd='12345', db='test_db')
cursor = db.cursor()
db.commit()
db.close()