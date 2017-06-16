import os, subprocess, csv, json

#===================================== showint.py ======================================#

#Saving the vppctl command in a variable first for future use
commd = "sudo vppctl show interface | column -t"
pcs = subprocess.Popen(commd, shell = True, stdout=subprocess.PIPE)
result = pcs.communicate()[0]


#Print results to a text file for future use
file = open('showintresult.txt', 'w')
print >>file, result
file.close()

#Setting delimiters for the fields to commas (from spaces)
output =  os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/todo-api/showintresult.txt").read()


#Saving output to .csv format for translation to  JSON format
file = open('showintresult.csv', 'w')
print >>file, output
file.close()


#Using .dump to translate .csv to .json row by row, and saving output to a file
with open('showintresult.csv') as file:
        read = csv.DictReader(file)
        rows = list(read)

json.dump(rows, open("showintresult.json", "w"), indent=4)

#Removing .txt and .csv files (no longer needed)
subprocess.call("rm -rf showintresult.txt showintresult.csv", shell = True)

#=======================================================================================#



#===================================== showbuff.py ======================================#


#Saving the vppctl command in a variable first for future use
commd = "sudo vppctl show buffers | column -t"
pcs = subprocess.Popen(commd, shell = True, stdout=subprocess.PIPE)
result = pcs.communicate()[0]


#Print results to a text file for future use
file = open('showbuffresult.txt', 'w')
print >>file, result
file.close()

#Setting delimiters for the fields to commas (from spaces)
output =  os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/todo-api/showbuffresult.txt").read()

#Saving output to .csv format for translation to  JSON format
file = open('showbuffresult.csv', 'w')
print >>file, output
file.close()


#Using .dump to translate .csv to .json row by row, and saving output to a file
with open('showbuffresult.csv') as file:
        read = csv.DictReader(file)
        rows = list(read)

json.dump(rows, open("showbuffresult.json", "w"), indent=4)

#Removing .txt and .csv files (no longer needed)
subprocess.call("rm -rf showbuffresult.txt showbuffresult.csv", shell = True)
#=======================================================================================#




#===================================== vpp.py ======================================#

terminal= "sudo vppctl show ip arp | column -t"
proc = subprocess.Popen(terminal,shell=True, stdout=subprocess.PIPE)
outp = proc.communicate()[0]

r= open('setip.txt', 'w')
print >>r, outp
r.close()


result = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/todo-api/setip.txt").read()


r = open('setip.csv', 'w')
print >>r, result
r.close

with open('setip.csv') as r:
        var = csv.DictReader(r)
        rows = list(var)

json.dump(rows, open("setip.json", "w"), indent=4)

#Removing .txt and .csv files (no longer needed)
subprocess.call("rm -rf setip.txt setip.csv", shell = True)
#=======================================================================================#





#===================================== read.py ======================================#

#run vpp command
cmd = "sudo vppctl show bridge-domain | column -t"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
output = ps.communicate()[0]

#output into a text file
o = open('bridge.txt', 'w')
print >>o, output
o.close()

#readying txt for json
toutput = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/todo-api/bridge.txt").read()

#translate to json
o = open('bridge.csv', 'w')
print >>o, toutput
o.close()

#.csv to .json translation
with open('bridge.csv') as o:
        reader = csv.DictReader(o)
        rows =  list(reader)
json.dump(rows, open('bridge.json', 'w'), indent=4)

#Removing .txt and .csv files (no longer needed)
subprocess.call("rm -rf bridge.txt bridge.csv", shell = True)
#=======================================================================================#




#===================================== read2.py ======================================#

#run vpp command
cmd = "sudo vppctl show hardware-interfaces | column -t"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
output = ps.communicate()[0]

#output into a text file
o = open('show.txt', 'w')
print >>o, output
o.close()

#readying txt for json
toutput = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/todo-api/show.txt").read()

#translate to json
o = open('show.csv', 'w')
print >>o, toutput
o.close()

#.csv to .json translation
with open('show.csv') as o:
        reader = csv.DictReader(o)
        rows =  list(reader)
json.dump(rows, open('show.json', 'w'), indent=4)

#Removing .txt and .csv files (no longer needed)
subprocess.call("rm -rf show.txt show.csv", shell = True)
#=======================================================================================#
