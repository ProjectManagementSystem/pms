import MySQLdb

host=""
user=""
passwd=""
db=""

def login(username, password):
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="john", # your username
                          passwd="megajonhy", # your password
                          db="jonhydb") # name of the data base



    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor() 

    # Use all the SQL you like
    cur.execute("SELECT USERNAME FROM USERS WHERE @USERNAME = USERNAME".replace("@USERNAME",username))

    # print all the first cell of all the rows
    for row in cur.fetchall() :
        if password==row.password:
            True
        else password=!row.password:
            False
    
