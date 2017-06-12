import os, subprocess, csv, json

#Saving the vppctl command in a variable first for future use
commd = "sudo vppctl show interface | column -t"
pcs = subprocess.Popen(commd, shell = True, stdout=subprocess.PIPE)
result = pcs.communicate()[0]


#Print results to a text file for future use
file = open('showintresult.txt', 'w')
print >>file, result
file.close()


#Setting delimiters for the fields to commas (from spaces)
output =  os.popen("awk '{$1=$1}1' OFS=, /home/sti/showintresult.txt").read()



#Saving output to .csv format for translation to  JSON format
file = open('showintresult.csv', 'w')
print >>file, output
file.close()


#Using .dump to translate .csv to .json row by row, and saving output to a file
with open('showintresult.csv') as file:
        read = csv.DictReader(file)
        rows = list(read)

json.dump(rows, open("showintresult.json", "w"), indent=4)