# http://sourceforge.net/projects/mysql-python/ MySQLdb module for python 2.7
import MySQLdb

con = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="admin", # your username
                      passwd="password", # your password
                      db="test") # name of the data base

sqlFile = open("initialise.sql","r")
sql = "".join(sqlFile.readlines())
cur = con.cursor()
cur.execute(sql)
#con.commit()
sqlFile.close()
con.close()

#import cx_Oracle
#con = cx_Oracle.connect('system/mypasswd@127.0.0.1/orcl')
#cur = con.cursor()
#cur.execute('start ./initialise.sql')
