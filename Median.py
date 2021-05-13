import csv
with open("H-W.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    nnumber=filedata[i][1]    
    newdata.append(nnumber)
n=len(newdata)
newdata.sort()
if n%2==0 :
    Median1=float(newdata[n//2])
    Median2=float(newdata[n//2-1])
    median=(Median1+Median2)/2
else :
    median=newdata[n//2]
    print(n)
print("Median is="+str(median))    