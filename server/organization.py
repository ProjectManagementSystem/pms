from logindb import loginwrite as info
import MySQLdb



def CreateOrganization(name, email, webpage, phone, logo_path, debug = False):

	db = MySQLdb.connect(host=info.host,

						 user=info.username, 
						  passwd=info.password, 
						  db=info.db)
	
	
	
	cur = db.cursor() 	
	sql = "INSERT INTO organization(oid,name, email, webpage, phone, logopath) VALUES (10,'@1', '@2', '@3', @4, '@5')"

	sql = sql.replace("@1",name)
	sql = sql.replace("@2",email)
	sql = sql.replace("@3",webpage)
	sql = sql.replace("@4",str(phone))
	sql = sql.replace("@5",logo_path)
	result = False
	if( debug == False):
		try:
			cur.execute(sql)
			db.commit()
			result = True
		except:
			result = False
	else:
		cur.execute(sql)
		db.commit()
		result = True
	db.close()
	return result;
result = CreateOrganization("A","a@b.com","www.x.com",123123,"logo.gif")
print "CreateOrganization() = " + str(result)
