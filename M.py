def maximalize(text):
	chrlist = sorted([c for c in text])
	la,continue_twice = False,False
	maximalized_text = ""
	for i in range(len(chrlist)-1,0,-1):
		if(continue_twice):
			continue_twice = False
			continue
		if(chrlist[i]==chrlist[i-1] and chrlist[i]!="z"):
			maximalized_text+=chr(ord(chrlist[i])+1)
			continue_twice = True
			if(i==1):
				la = True
			continue
		maximalized_text+=chrlist[i]
	if(not la):
		maximalized_text += chrlist[0]
	return(maximalized_text)
 
comp = maximalize(input())
temp = comp
while(True):
	comp = maximalize(temp)
	if(comp==temp):
		break
	else:
		temp = comp
print(comp)
