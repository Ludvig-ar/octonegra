print "Cleaning Haproxy settings"
infile = "/etc/haproxy/haproxy.cfg"
outfile = "/home/pi/octonegra/haproxy.cfg"
replace_list = ["negra","cordobesa"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
	for word in replace_list:
		line=line.replace(word, "*")
	fout.write(line)
fin.close()
fout.close()
print "Cleaning octoprint config..."
infile = "/home/pi/.octoprint/config.yaml"
#infile ="testfile.txt"
outfilet="/home/pi/octonegra/configt.yaml"
outfile="/home/pi/octonegra/config.yaml"
fin = open(infile)
fout = open(outfilet,"w+")
#Borra key
for line in fin:
	tenchars = line.strip()
        initial = tenchars[0:3]
	if ("key"==initial):
		linechanged="Hidden Key"+"\n"
	else:
		linechanged=line
	fout.write(linechanged)
fin.close()
fout.close()
#Borra Token
fin=open(outfilet)
fout=open(outfile,"w+")
for line in fin:
	tenchars = line.strip()
        initial = tenchars[0:5]
	if ("token"==initial):
		linechanged="Hidden Token"+"\n"
	else:
		linechanged=line
	fout.write(linechanged)
fin.close()
fout.close()
import os
os.remove(outfilet)
