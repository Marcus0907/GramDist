import re

res = {}

def count(pattern_list):

    for i in pattern_list:
        if i.split("_")[0] not in res:
            res[i.split("_")[0]] = "_" + str(i.split("_")[1]) + "_" + str(i.split("_")[1])
        else:
            if i.split("_")[-1] == "Y":
                res[i.split("_")[0]] = "_" + str(int(res[i.split("_")[0]].split("_")[1]) + int(i.split("_")[1])) + "_" + str(int(res[i.split("_")[0]].split('_')[2]) + int(i.split("_")[1]))
            else:
                res[i.split("_")[0]] = "_" + str(int(res[i.split("_")[0]].split("_")[1]) + int(0)) + "_" + str(int(res[i.split("_")[0]].split('_')[2]) + int(i.split("_")[1]))

    return (res)




pattern_list= []
with open('Gram-positive-576-Train_Patterns.txt')as file:
    lines = file.readlines()
    for i in lines:
        pattern = i.strip("\n")
        # print(pattern)

        pattern_list.append(pattern)

# print(pattern_list)
last_closedpattern = count(pattern_list)
file = open('Gram-positive-576-Train_Last_Patterns.txt','a',encoding="utf-8")
flag = 0
for i in last_closedpattern:
    file.write(str(i)+last_closedpattern[i]+"\n")
    print(flag)
    flag += 1
    # print(str(i)+last_closedpattern[i])
file.close()
# last_pattren = count(pattern_list)
# print(last_pattren)
