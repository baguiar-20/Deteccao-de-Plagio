#processo para remover comentarios


print("Codigo antes:\n")
filepath = 'arquivo.txt'
with open(filepath, "r+") as fp:
   for cnt, line in enumerate(fp):
       print( line)

print("Processo de remocao de comentarios:\n")

filepath = 'arquivo.txt'
j = 0
with open(filepath, "r+") as fp:
   for cnt, line in enumerate(fp):
       #print(line)
       for i in range(len(line)):
           if(line[i]  == '/' and line[i+1] == "*"):
               j = i +1
               while(line[j] != "*" and line[i] != "/"):
                    print(line[j])
                    #line = line.replace(line[j], "")
                    j+=1



print("Codigo depois:\n")
'''
filepath = 'arquivo.txt'
with open(filepath, "r+") as fp:
   for cnt, line in enumerate(fp):
       print("Line {}: {}".format(cnt, line))
       '''