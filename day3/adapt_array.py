f = open("input.txt","r")
o = open("good_input.txt","w+")

for line in f.readlines():
	st = "\""
	for char in line:
		if char != ',':
			st += char
		else:
			o.write(st + "\",")
			st = "\""
	o.write(st + "\"")
	st = ""
	o.write("\n")

f.close()
o.close()
