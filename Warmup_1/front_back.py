def front_back(str):
	if len(str)<=1:
		return str
	else :
		first= str[0]
		last= str[len(str)-1]
		return last+ str[1:len(str)-1] + first
