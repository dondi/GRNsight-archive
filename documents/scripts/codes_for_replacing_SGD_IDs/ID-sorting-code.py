import re
stem_lines = []
newlist = []
syslist = []
sgdlist = []
somelist = []
with open("/Users/ahmad00.m/Desktop/re-testing data/wt_stem_computedaverage.txt") as f:
    data = f.readlines()
    count = 0
    for i in data:
        stem_lines.append(i.split())
        
    dict = {}
    for z in stem_lines:
        key = tuple(z[1:])
        if key not in dict:
            dict[key] = [z[0]]
        else:
            dict[key].append(z[0])
            
    sys = re.compile("Y[A-P][LR][0-9][0-9][0-9][WwCc](-[A-Z])?")
    sgd = re.compile("SGD:S0000[0-9][0-9][0-9][0-9][0-9]")
    
with open("/Users/ahmad00.m/Desktop/re-testing data/resultof-ID-sorting-code.txt", "a") as textfile:
    for x, y in dict.items():
        # print(y)
        if len(y) > 1:
            sys_list = list(filter(sys.match, y))
            # sta_list = not list(filter(sgd.match, y)) and not list(filter(sys.match, y))
            sgd_list = list(filter(sgd.match, y)) 
            if len(sys_list) == 1: # this should return systematic names
                newlist = sys_list + list(x)
                fields = '\t'.join(newlist)
                textfile.write(fields)
                textfile.write('\n')
            elif len(sys_list) > 1: # this should return systematic names
                newlist = [] 
                for i in sys_list:
                    newlist = []
                    newlist.append(i)
                    anotherlist = newlist + list(x)
                    fields = '\t'.join(anotherlist)
                    textfile.write(fields)
                    textfile.write('\n')
            elif len(sgd_list) >= 1: # this should return SGD names     
                newlist = sgd_list + list(x)
                fields = '\t'.join(newlist)
                textfile.write(fields)
                textfile.write('\n')
            else: # this should return SGD names 
                newlist = sgd_list + list(x)
                fields = '\t'.join(newlist)
                textfile.write(fields)
                textfile.write('\n')
        
        elif len(y) == 1:
            newlist = y + list(x)
            fields = '\t'.join(newlist)
            textfile.write(fields)
            textfile.write('\n')
            
        
