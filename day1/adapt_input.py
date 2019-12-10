f = open("input.txt","r")
h = open("haskell_input.txt","w+")

h.write("[")
for line in f.readlines():
	h.write(line[:-1])
	h.write(",")

f.close()
h.close()
