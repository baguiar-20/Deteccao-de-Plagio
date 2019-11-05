import re 
filepath = 'arquivo.txt'


print(" ------ Codigo antes -----")

with open(filepath, 'r') as fp:
    line = fp.readline()
    while line:
       line = fp.readline()
       print(line)

fp.close()

print("---- Codigo com os comentarios removidos -----")
#ele ja desconsidera a primeira linha do codigo em c

with open(filepath, 'r+') as fp:
   line = fp.readline()
   while line:
       line = fp.readline()
       string = line
       string = re.sub(r'\/.+\/', "", string)
       print(string)
fp.close()