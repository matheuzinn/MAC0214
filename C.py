input()
tp = input()
cl = False
text = ""
for _ in range(int(input())):
	pkey = input()
	if(pkey == "Backspace"):
		text = text[:-1]
		continue
	elif(pkey == "CapsLock"):
		cl = not cl
		continue
	elif(pkey == "Space"):
		text += " "
		continue
	if(cl):
		text += pkey.upper()
		continue
	text += pkey.lower()
print("Correct" if text == tp else "Incorrect")
