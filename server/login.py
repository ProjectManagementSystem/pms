import MySQLdb

from logindb import loginread as info


def login(email, password):
    db = MySQLdb.connect(host=info.host , # your host, usually localhost
                         user=info.username, # your username
                          passwd=info.password, # your password
                          db=info.db) # name of the data base



    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor() 

    # Use all the SQL you like
    cur.execute("SELECT password FROM USERS WHERE '@email' = email".replace("@email",email))

    if password == cur.fetchall()[0][0]:
        db.close()
        return True
    else:
        db.close()
        return False
