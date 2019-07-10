def patterns(num,s):
    snip=[]
    for i in range(len(s)):
        if (len(s[i:i+num])==num):
            snip.append(s[i:i+num])
    return snip

def list_all_dict(s):
    res = {}
    result = []
    for i in range(1,len(s)):
        res[i] = patterns(i,s)
        dict={}
        for key in res[i]:
            dict[key] = dict.get(key,0)+1
        dict_last = {i:dict[i] for i in dict if dict[i]>1}
        if dict_last:
            result.append(dict_last)
    return result

def closed_pattern(result_all):
    list_copy =[]
    for i in result_all:
        dict_copy = {}
        for key,value in i.items():
            dict_copy[key] = str(value)+"_Y"
        list_copy.append(dict_copy)
    for i in range(1,len(result_all)):
        myDict = result_all[i]
        for key,value in myDict.items():
            prior = key[0:len(key)-1]
            post = key[1:len(key)]

            prior_dict = result_all [i-1]
            if prior in prior_dict.keys() and post in prior_dict.keys():

                if myDict[key] == prior_dict[prior]:
                    list_copy[i-1][prior] = list_copy[i-1][prior].replace("Y","N")
                if myDict[key] == prior_dict[post]:
                    list_copy[i-1][post] = list_copy[i-1][post].replace("Y","N")
    return list_copy


seq = []
with open('Training-New/Gram-negative-1591-Train.txt','r') as f:
    content = f.readlines()
    for each in content:
        seq.append(each.strip('\n'))
for i in seq:
    id = i.split(',')[0]
    x = i.split(',')[1]

    pattern_x = []
    pattren_results = []
    result_all = list_all_dict(x)
    last = closed_pattern(result_all)
    print(last[1::])

    print(x+i.split(',')[0])

    concatnate_id = str(id)+'#'+str(x)+'#'
    concatnate_list = []
    for i in last:
        for key in i.keys():
            if len(key)>1:
                concatnate_list.append(str(key)+'_'+str(i[key]))
    concatnate_str = ','.join(concatnate_list)
    concatnate_result = concatnate_id+concatnate_str
    print(concatnate_result)
    files = open('Gram-negative-1591-Train_ClosedPatterns.txt','a',encoding="utf-8")
    files.write(concatnate_result+'\n')

    for i in concatnate_list:
        print(i)
        file = open('Gram-negative-1591-Train_Patterns.txt','a',encoding="utf-8")
        file.write(i+'\n')
files.close()
file.close()









































