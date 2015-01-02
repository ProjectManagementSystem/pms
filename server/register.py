# [DA] commits
import MySQLdb

# var size limits: userid => [8]??, name - surname - phone - facebookid => char[128], password => char[512] primarykey (userid)
from logindb import loginwrite as info

debug = 1

def register (u_name, u_surname, u_mail, u_pass, u_phone, u_facebookid):
    # connect to database, send the params
    db = MySQLdb.connect(host =  info.host, user = info.username , passwd = info.password , db = info.db)
    # can take queries now
    cur = db.cursor()
    # first, try to insert this info to the database

    if debug:
        if not cur.execute("SELECT (1) FROM USERS WHERE EMAIL = %s", (u_mail)):
            cur.execute("""INSERT INTO USERS(NAME, SURNAME, EMAIL, PASSWORD, PHONE, FACEBOOKID)
                                       VALUES(%s, %s, %s, %s, %s, %s)""", (u_name, u_surname, u_mail, u_pass, u_phone, u_facebookid))
            db.commit()
        else:
            print "Same email encountered, nothing added."
    else:
        try:
            if not cur.execute("SELECT (1) FROM USERS WHERE EMAIL = %s", (u_mail)):
                cur.execute("""INSERT INTO USERS(NAME, SURNAME, EMAIL, PASSWORD, PHONE, FACEBOOKID)
                                       VALUES(%s, %s, %s, %s, %s, %s)""", (u_name, u_surname, u_mail, u_pass, u_phone, u_facebookid))
                db.commit()
        except:
            db.rollback()
            return False
    return True