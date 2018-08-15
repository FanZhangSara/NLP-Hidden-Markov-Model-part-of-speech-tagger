import sys
file1 = sys.argv[1]
# def lastchara(str):
#     words = str.split("*")
#     word = words[-1]
#     return word
import json
with open("hmmmodel.txt","r") as f:
    data = f.read()
    model = data.split('\n')
    dict = json.loads(model[0])
    dictletter = json.loads(model[1])
    listchara = json.loads(model[2])
# dict =model[0]
# dictletter = model[1]
# listchara = model[2]
listchara = listchara['list']
#print("dictdictdict")
#print(dict)

# with open("dictletter_f.json","r") as f:
#     data = f.read()
#     dictletter = json.loads(data)
# #print("dictletterdictletterdictletter")
# #print(dictletter)
#
# with open("list1.json","r") as f:
#     data = f.read()
#     listchara = json.loads(data)
#print("listcharalistcharalistchara")
listchara.remove('q')
listchara.remove('qend')
# print(listchara)
#print(len(listchara))
#
file = open("hmmoutput.txt","w")



with open(file1) as f:
  content = f.readlines()
#   print(content)
#  length = len(letter)
#   #each line
  for x in content:
      x = x.strip('\n')
      word = x.split(" ")
      #print(word)
      table = [[0 for i in range(len(word)+1)] for j in range(len(listchara))]
      pointer = [[0 for i in range(len(word)+1)] for j in range(len(listchara))]
     # print(table)
     # print(len(table))


      for i in range(len(word)+1):
          if i in range(1,len(word)):
              for j in range(len(listchara)):
                  max1 = 0
                  for r in range(len(listchara)):
                      # word[i] state:list[j] previous state:list[r]
                      #max1 = 0
                      if word[i] in dictletter:
                          if listchara[j] in dictletter[word[i]]:
                              a = dict[listchara[r]][listchara[j]]
                              b = dictletter[word[i]][listchara[j]]
                              c = table[r][i - 1]
                              value = table[r][i - 1] * dict[listchara[r]][listchara[j]] * dictletter[word[i]][listchara[j]]
                          else:
                              value = 0
                      else:
                          value = table[r][i - 1] * dict[listchara[r]][listchara[j]]

                      if value > max1:
                          table[j][i] = value
                          max1 = value
                          pointer[j][i] = r
          if i == 0:
              for j in range(len(listchara)):
                  if word[i] in dictletter:
                      if listchara[j] in dictletter[word[0]]:
                          table[j][i] = dict['q'][listchara[j]] * dictletter[word[i]][listchara[j]]
                      else:
                          table[j][i] = 0
                  else:
                      table[j][i] = dict['q'][listchara[j]]

          if i == len(word):
              for j in range(len(listchara)):
                  table[j][i] = dict[listchara[j]]['qend']*table[j][i-1]


      #print(table)

      max = 0
      m = 0
      n = 0
      for i in range(len(listchara)):
          if table[i][len(word)] > max:
              m = i
              n = len(word)
              max = table[i][len(word)]
      #print("nnnnn")
      #print(n)
      n = n-1
      listtag = []
      while n>=0:
          listtag.append(listchara[m])
          m = pointer[m][n]
          n = n-1

      #print("listcharalistcharalistchara")
     # print(listtag)
      for i in range(len(word)):
          if i == len(word)-1:
              file.write(word[i])
              file.write('/')
              file.write(listtag[len(word) - 1 - i])
              file.write('\n')
          else:
              file.write(word[i])
              file.write('/')
              file.write(listtag[len(word) - 1 - i])
              file.write(" ")



file.close()

      # for d1 in range(6):
      #     for d2 in range(6):
      #         table[d1][d2] = d1 + d2 + 2

      # #each word
      # for j in range(len(word)):
      #     worddict = list(dictletter[word[j]].keys())  # (vb * vb)
      #     #word[j]
      #     #worddict list
      #     print(worddict)
      #     print('\n')
      #     match = list(dictmatch.keys())
      #     for i in match:
      #         for y in worddict:
      #             value = dictmatch[i] * dictletter[word[j]][y] * dict[lastchara(i)][y]
      #             str = i,y
      #             dictmatch[str] = value
      #         dictmatch.pop(i)
      #
      #
      #     maxmatch = list(dictmatch.keys())
      #     for i in maxmatch:

 #                 value = dictmatch[i] * dictletter[word[j]][y] * dict[lastchara(i)][y]
 #                 if(value > maxvalue):
 #                     maxvalue = value
 #                     final = i,'*',y



  #    table = [[0 for i in range(len(word))] for j in range(len(letter))]
 #     for d1 in range(len(letter)):
   #       for d2 in range(len(word)):
    #          table[d1][d2] = d1 + 2
     # print(table)
      #print(table[0][1])
