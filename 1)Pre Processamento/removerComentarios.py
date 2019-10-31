
import nltk
#nltk.download('punkt')
import os

arq = open("arquivo.txt", "r+")

i = 0
j = 0
comentario = []
for linha in arq:
    l = nltk.word_tokenize(linha)
    for i in range(len(l)-1):
        if(l[i] == '/*'):
            j = i
            while(l[j] != '*/'):
                print(l[j])
                #arq = arq.replace(l[j], "")
                j +=1
   