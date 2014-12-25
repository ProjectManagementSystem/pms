# [DA] commits
#import time
#import random
#import socket
#import hashlib
import MySQLdb
"""
#adds more randomness to the guid
UID_CONST1 = 0x7FFFFFFF
UID_CONST2 = 0x1337B8D8

def guid(*args):

    # Generates a universally unique ID.
    # Any arguments only create more randomness.

    t = long(time.time() * 1000)
    r = long(random.random() * 100000000000000000L)
    try:
        a = socket.gethostbyname(socket.gethostname())
    except:
        # if we can't get a network address, just imagine one
        a = random.random()*100000000000000000L
    data = str(t)+ ' ' + str(r) + ' ' + str(a) + ' ' + str(args)
    data = hashlib.md5(data).hexdigest()

    return data[:8]
"""
# var size limits: userid => [8]??, name - surname - phone - facebookid => char[128], password => char[512] primarykey (userid)

def register (u_name, u_surname, u_mail, u_pass, u_phone, u_facebookid, u_regdate):
    # connect to database, send the params
    db = MySQLdb.connect(host = "localhost", user = "Doruk", passwd = "bestpassever", db = "pms")
    # can take queries now
    cur = db.cursor()
    # first, try to insert this info to the database
    try:
        cur.execute("""INSERT INTO USERINFO(NAME, SURNAME, MAIL, PASS, PHONE, FACEBOOKID, REGISTERDATE)
                                   VALUES(%s, %s, %s, %s, %s, %s, %s)""", (u_name, u_surname, u_mail, u_pass, u_phone, u_facebookid, u_regdate))
        db.commit()
    except:
        db.rollback()
        return false
    return true