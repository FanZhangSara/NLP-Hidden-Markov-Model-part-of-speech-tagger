import sys
file = sys.argv[1]
# for i in range(1, len(sys.argv)):
# print （"", i, sys.argv[i]）
#print(content)
#dict_2d = {'a': {'a': 1, 'b': 3}, 'b': {'a': 6}}

total1 = 0
dict = {}
dictletter = {}
dictchara = {}
list11 = []
def addkey_value(key_a, key_b):
  if key_a in dict:
    if key_b in dict[key_a]:
      dict[key_a][key_b]+=1
    else:
      #dict[key_a] = {}
      dict[key_a][key_b] = 1
      #dict['key_a'].update({key_b: dict['key_a']['key_b'] + 1})
  else:
    dict[key_a] ={}
    dict[key_a][key_b] = 1
    #dict.update({key_a:{key_b: 1}})

def addletterkey_value(keya, keyb):
  if keya in dictletter:
    if keyb in dictletter[keya]:
      dictletter[keya][keyb] += 1
    else:
      dictletter[keya][keyb] = 1
  else:
    dictletter[keya] = {}
    dictletter[keya][keyb] = 1

def totalchara(key):
  if key in dictchara:
    dictchara[key] += 1
  else:
    global total1
    total1 = total1+1
    list11.append(key)
    dictchara[key] = 1


# read file line by line
with open(file) as f:
  content = f.readlines()
  #print(content[2])
  for x in content:
    x = x.strip('\n')
    # print("x")
    # print(x)
    # print("x")
 #   print(x)
    word = x.split(" ")
    # print(word)
    for j in range(len(word)):
      if j == 0:
        key_value = word[0].rsplit("/",1)
        addkey_value('q', key_value[1])
        if len(word) >1:
          key_value1 = word[j].rsplit("/",1)
          key_value2 = word[j + 1].rsplit("/",1)
          addkey_value(key_value1[1], key_value2[1])
      if j == len(word)-1:
        key_value = word[j].rsplit("/",1)
        addkey_value(key_value[1],'qend')
        # if key_value[1]==':':
        #   print(x)

      if j in range(1,len(word)-1):
        key_value1 = word[j].rsplit("/",1)
        key_value2 = word[j+1].rsplit("/",1)
        addkey_value(key_value1[1],key_value2[1])



  for y in content:
    y = y.strip('\n')
    word = y.split(" ")
#    print(word)
    for j in range(len(word)):
      key_value = word[j].rsplit("/",1)
      addletterkey_value(key_value[0],key_value[1])

  for z in content:
    z = z.strip('\n')
    word = z.split(" ")
    for j in range(len(word)):
      key = word[j].rsplit("/",1)
      totalchara(key[1])

#print("totalchara()")
list11.append('q')
list11.append('qend')
#print(list11)
total1 += 2
#print('/n')
#print("totalchara()totalchara()totalchara()totalchara()totalchara()totalchara()")
#print('/n')
#print(total1)

#print("dict")
#print(dict)
#print(dictletter)
number = {}
dict_f = {}
for x in dict:
#  dict_f[x] = {}
  total = 0
  for y in dict[x]:
    total += dict[x][y]
  #print(total)
  number[x] = total
#print("number")
#print(number)

for x in dict:
  dict_f[x] = {}
  for y in list11:
    if y in dict[x]:
      dict_f[x][y] = (dict[x][y]+1)/(number[x]+total1)
    else:
      dict_f[x][y] = 1/(number[x]+total1)
  # for y in dict[x]:
  #   dict_f[x][y] = dict[x][y]/number[x]
#print("dict_f")
#print(dict_f)

#print("dictletter")
#print(dictletter)
dictletter_f = {}
letter = {}
for x in dictletter:
  total = 0
  for y in dictletter[x]:
    total += dictletter[x][y]
  letter[x] = total
#print("letter")
#print(letter)

for x in dictletter:
  dictletter_f[x] = {}
  for y in dictletter[x]:
    dictletter_f[x][y] = dictletter[x][y]/dictchara[y]
#print(dictletter_f)


#print(dictchara)

import json
listdic={}
listdic["list"]=list11
jsObj1 = json.dumps(dict_f)
jsObj2= json.dumps(dictletter_f)
jsObj3 = json.dumps(listdic)

fileObject = open("hmmmodel.txt","w")
#fileObject = open("dict_f.json","w")
fileObject.write(jsObj1)
fileObject.write('\n')
fileObject.write(jsObj2)
fileObject.write('\n')
fileObject.write(jsObj3)

#fileObject.close()
# data = json.dumps(dict_f)
# with open("dict_f.json","w") as f:
#   f.write(data)

# jsObj = json.dumps(dictletter_f)
# fileObject = open("hmmmodel.txt","r+")
# fileObject.read()
# fileObject.write(jsObj)
# fileObject.write('\n')
# #fileObject.close()
# # import json
# # data = json.dumps(dictletter_f)
# # with open("dictletter_f.json","w") as f:
# #   f.write(data)
#
# jsObj = json.dumps(list11)
# fileObject = open("hmmmodel.txt","r+")
# fileObject.read()
# fileObject.write(jsObj)
# fileObject.close()
# # import json
# # data = json.dumps(list11)
# # with open("list1.json","w") as f:
# #   f.write(data)


#for word in words:
#print(word)