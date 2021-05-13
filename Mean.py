import csv
with open("H-W.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    nnumber=filedata[i][1]    
    newdata.append(float(nnumber))
n=len(newdata)
total=0
for x in newdata:
    total+=x
Mean=total/n
print("Mean is="+str(Mean))
        