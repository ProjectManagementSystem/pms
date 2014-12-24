import MySQLdb



def CreateOrganization(name, email, webpage, phone, logo_path):

	db = MySQLdb.connect(host="localhost",
						 user="john", 
						  passwd="megajonhy", 
						  db="john dalton")
	
	
	
	cur = db.cursor() 	
	sql = "INSERT INTO organization(name, email, webpage, phone, logopath) VALUES ('@1', '@2', '@3', '@4', '@5')"
	sql = sql.replace("@1",name)
	sql = sql.replace("@2",email)
	sql = sql.replace("@3",webpage)
	sql = sql.replace("@4",phone)
	sql = sql.replace("@5",logo_path)
	try:
		cur.execute(sql)
	except:
		return False;
	return True;
