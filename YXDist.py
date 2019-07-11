import os
import numpy as np
from decimal import *
import pandas as pd
import math
import matplotlib.pyplot as plt


Test = []
Gram_Ne = []
Gram_Po = []
csv = {"Ne_Dist":[],"Po_Dist":[]}
LastNe = []
LastPo = []


path = os.getcwd()+'/1'
files = os.listdir(path)
for each in files:
    path_dir = path + '/{}'.format(each)

    with open(path_dir,mode='r',encoding='utf-8') as f:
        lines = f.readlines()
        for i in lines:
            Test.append([i.split(",")[0],float(i.split(",")[1])])
    # print(Test)

    # with open("./Gram_Ne_Train/GN3/Gram-Negative-Train-3.txt") as f:
    with open("Gram-Negative-Train-1.txt") as f:
        lines = f.readlines()
        for i in lines:
            Gram_Ne.append([i.split("_")[0],float(i.split("_")[1])])
    # print(Gram_Ne)

    # with open("./Gram_Ne_Train/GN3/Gram-Positive-576-Train.txt") as f:
    with open("Gram-Positive-576-Train.txt") as f:
        lines = f.readlines()
        for i in lines:
            Gram_Po.append([i.split("_")[0],float(i.split("_")[1])])
    # print(Gram_Po)

    dict_Test = {i[0]:i[1] for i in Test}
    dict_Ne ={i[0]:i[1] for i in Gram_Ne}
    dict_Po = {i[0]:i[1] for i in Gram_Po}

    dictBothNe = {i:abs(dict_Ne[i]-0) for i in dict_Test if i in dict_Ne and i in dict_Po}
    dictTest = {i:abs(dict_Test[i]-0) for i in dict_Test if i in dict_Ne and i in dict_Po}

    dictBothPo = {i:abs(dict_Po[i]-0) for i in dict_Test if i in dict_Ne and i in dict_Po}
    # dictNe1 = {i:dict_Test[i] for i in dict_Test if i not in dict_Ne}
    # dictNe2 = {i:dict_Ne[i] for i in dict_Ne if i not in dict_Test}
    # dict_NeDif = dict(dictBothNe)
    # dict_NeDif.update(dictNe1)
    # dict_NeDif.update(dictNe2)
    La_Ne = {i:abs(dict_Test[i]* dict_Ne[i]) for i in dict_Test if i in dict_Ne and i in dict_Po}
    La_Po = {i:abs(dict_Test[i]* dict_Po[i]) for i in dict_Test if i in dict_Po and i in dict_Ne}
    SumNe = 0
    SumTest = 0
    La_Ne_sum = []
    La_Po_sum = []
    for i in La_Ne:
        La_Ne_sum.append(La_Ne[i])
    NumNe = sum(La_Ne_sum)
    for i in La_Po:
        La_Po_sum.append(La_Po[i])
    NumPo = sum(La_Po_sum)
    for item in dictBothNe:
        # if len(item)  == 3:
        if len(item) > 2 :
            # print(item)
            SumNe = SumNe + (float(dictBothNe[item]) ** 2)
    for item in dictTest:
        if len(item) > 2 :
            SumTest = SumTest + (float(dictTest[item]) ** 2)



    # dictPo1 = {i:dict_Test[i] for i in dict_Test if i not in dict_Po}
    # dictPo2 = {i:dict_Po[i] for i in dict_Po if i not in dict_Test}
    # dict_PoDif = dict(dictBothPo)
    # dict_PoDif.update(dictPo1)
    # dict_PoDif.update(dictPo2)
    SumPo = 0
    for item in dictBothPo:
        # if len(item)  == 3:
        if len(item) > 2 :

            SumPo = SumPo + (float(dictBothPo[item]) ** 2)

    LastResultNe = NumNe/((math.sqrt(SumNe))*(math.sqrt(SumTest)))
    LastResultPo = NumPo/((math.sqrt(SumPo))*(math.sqrt(SumTest)))

    print(Decimal(math.sqrt(LastResultNe)).quantize(Decimal('0.0000')),Decimal(math.sqrt(LastResultPo)).quantize(Decimal('0.0000')))
    # print(Decimal(math.sqrt(SumPo)).quantize(Decimal('0.0000')))
#     LastNe.append(Decimal(math.sqrt(SumNe)).quantize(Decimal('0.0000')))
#     LastPo.append(Decimal(math.sqrt(SumPo)).quantize(Decimal('0.0000')))
#     csv["Ne_Dist"].append(Decimal(math.sqrt(SumNe)).quantize(Decimal('0.0000')))
#     csv["Po_Dist"].append(Decimal(math.sqrt(SumPo)).quantize(Decimal('0.0000')))
# df=pd.DataFrame(csv)
# print(LastNe)
# print(LastPo)
# df.to_csv("Gram-Positive_Result_1_D_3.csv",index=False , header= True)

plt.plot(LastPo, label='Po_Distance')
plt.plot(LastNe, label='Ne_Distance')
plt.xlabel('No.')
plt.ylabel('Distance')
# plt.xlim((1, 61))
plt.title("Gram-NE")
axes = plt.gca()
# axes.set_ylim([830,900])
plt.legend()
# plt.savefig('GramNE.png', dpi=900)
plt.show()

# plt.bar(x, LastNe, width=width, label='Positive_Distance',fc='y')
# plt.bar(x + width, LastPo, width=width, label='Negative_Distance',fc='b')