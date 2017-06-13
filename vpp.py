import os, subprocess, csv, json

terminal= "sudo vppctl show ip arp | column -t"
proc = subprocess.Popen(terminal,shell=True, stdout=subprocess.PIPE)
outp = proc.communicate()[0]

r= open('setip.txt', 'w')
print >>r, outp
r.close()


result = os.popen("awk '{$1=$1}1' OFS=, /home/sti/todo-api/setip.txt").read()


r = open('setip.csv', 'w')
print >>r, result
r.close

with open('setip.csv') as r:
        var = csv.DictReader(r)
        rows = list(var)

json.dump(rows, open("setip.json", "w"), indent=4)
