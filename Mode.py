from collections import Counter
import csv
with open("H-W.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    nnumber=filedata[i][1]    
    newdata.append(nnumber)
data=Counter(newdata)
modedatarange={"50-60":0,"60-70":0,"70-80":0}    
for weight,occurence in data.items():
    if 50<float(weight)<60:
        modedatarange["50-60"]+=occurence
    elif 60<float(weight)<70:
        modedatarange["60-70"]+=occurence
    elif 70<float(weight)<80:
        modedatarange["70-80"]+=occurence
moderange,modeoccurence=0,0
for range,occurence in modedatarange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence    
Mode=float((moderange[0]+moderange[1])/2)
print(Mode)    