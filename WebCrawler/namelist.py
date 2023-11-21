import csv
import pandas as pd
f = "devg1.csv"
rows = []
dg = []
oldurl = ''
with open(f, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

for i in range(1,len(rows)):
    oldurl = str(rows[i])
    newurl = oldurl.split("/").pop()
    dg.append(newurl[0:-2])

dict = {'Developer Name':dg}
df = pd.DataFrame(dict)
df.to_csv('opq.csv')