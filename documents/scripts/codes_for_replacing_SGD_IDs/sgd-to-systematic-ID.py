yeastmine = open("/Users/ahmad00.m/Desktop/exp_data_cleaning/YeastNomenclature.txt")
template = open("/Users/ahmad00.m/Desktop/exp_data_cleaning/SGD_CORRECT_format.txt")
newfile = open("/Users/ahmad00.m/Desktop/exp_data_cleaning/replaced_SYS_IDs.txt","w")

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
