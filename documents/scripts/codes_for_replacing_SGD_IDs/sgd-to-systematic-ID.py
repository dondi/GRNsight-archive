yeastmine = open("/Users/ahmad00.m/Desktop/re-testing data/YeastNomenclature.txt")
template = open("/Users/ahmad00.m/Desktop/re-testing data/result-of-SGD-remover.txt")
newfile = open("/Users/ahmad00.m/Desktop/re-testing data/result-ofsgd-to-systematic-ID.txt","w")

templateDict = dict()
for line in yeastmine:
    lineList = line.split("\t")
    templateDict[lineList[0]] = lineList[1]
for line in template:
    sighlist = line.split("\t")
    for key in templateDict:
        if key == sighlist[0]:
            anotherline = line.replace(sighlist[0],templateDict[key])
            newfile.write(anotherline) 

newfile.close()