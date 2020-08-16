import sqlite3
print("Welcome to dev-sqlite3 terminal by Dev Gupta[GitHub:coderdev04]\nType \";\" to end statement, type \"exit;\" to quit.")
db_name=input("enter database name[without extention]:")
try:
	db_name+=".db"
	conn=sqlite3.connect(db_name)
	c=conn.cursor()
	print("connected successfully!")
	cmd=""
	while (cmd!="exit;"):
		cmd=input("dev-sqlite3>")
		while(cmd[-1]!=";"):
			cmd+=input("          ->")
		#print(cmd)
		try:
			c.execute(cmd)
			#print(cmd[0:6].lower())
			if(cmd[0:6].lower()=="select"):
				#print("selected")
				res=c.fetchall()
				for x in res:
					print(x)
			else:
				conn.commit()
		except Exception as e:
			print(str(e))
	
	print("exit!")
except:
	print("unable to connect!")
