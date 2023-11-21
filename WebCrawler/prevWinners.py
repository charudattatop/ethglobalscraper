import pandas as pd
filename = "opq.csv"
fname = "onlynames.csv"
d1 = pd.read_csv(fname)
data = pd.read_csv(filename)

cname = 'Developer Name'
carray = data[cname].values
check = d1[cname].values

prevwin = []
for i in range(len(carray)+1):
    if check[i] in carray:
        prevwin.append(check[i])

dict = {'Developer Name' : prevwin}
df = pd.DataFrame(dict)
df.to_csv('PrevContestant.csv')
