import redis
import random, string

r = redis.Redis(host='127.0.0.1',port=6379,db=0)
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
		r.lpush('code',temp)





