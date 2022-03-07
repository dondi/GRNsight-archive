list1 = [] 
list2 = []
k = []
with open("/Users/ahmad00.m/Desktop/exp_data_cleaning/SGD_incorrect_format.txt") as file:
    with open("/Users/ahmad00.m/Desktop/exp_data_cleaning/SGD_CORRECT_format.txt", "w") as something:
        data = file.readlines()
        for i in data:
            x = (i.split())
            newlist = [i.replace('SGD:','') for i in x]
            fields = '\t'.join(newlist)
            something.write(fields)
            something.write('\n')
            
