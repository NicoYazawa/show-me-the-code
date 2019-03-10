import mysql.connector
import random, string

chars = string.ascii_uppercase + string.digits
active_code=[]
while len(active_code)!=200:
	temp = ''
	s = random.sample(chars,20)
	for j in range(20):
		if j%4 ==0 and j!=0:
			temp=temp+'-'+s[j]
		else:
			temp=temp+s[j]
	if temp not in active_code:
		active_code.append(temp)

mydb =mysql.connector.connect(
	host="localhost",
	user="User_Name",
	passwd="Your_PassWord",
	database="activate_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE activate_code (id INT(3), code VARCHAR(100))")

sql = "INSERT INTO activate_code(id, code) VALUES (%s, %s)"
for i in range(len(active_code)):
	val = (i,active_code[i])
	mycursor.execute(sql, val)
	
mydb.commit()
