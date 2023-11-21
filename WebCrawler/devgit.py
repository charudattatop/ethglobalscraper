import csv
import pandas as pd
f = "output.csv"
f1 = "devg1.csv"
rows = []
dg = []
oldurl = ''
with open(f, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

for i in range(1,len(rows)):
    oldurl = str(rows[i])
    print(oldurl)
    newurl = oldurl[2:]
    print(newurl)
    newurl = "/".join(newurl.split("/")[:-1])
    dg.append(str(newurl))


dict = {'Developer Link':dg}
df = pd.DataFrame(dict)
df.to_csv('devg1.csv')

