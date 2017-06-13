import os, subprocess, csv, json

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
