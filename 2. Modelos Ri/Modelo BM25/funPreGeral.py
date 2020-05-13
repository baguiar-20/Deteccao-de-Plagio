
#troca os simbolos por tokens

def tokensSimbolos(texto, tokens): 
    x = ' '
    k = ' '
    for i in range(len(texto)):
        texto[i] = texto[i].replace("::" ,"tg")
        texto[i] = texto[i].replace("&&" ,"ob")
        texto[i] = texto[i].replace("||" ,"oc")
        texto[i] = texto[i].replace("<<" ,"js")
        texto[i] = texto[i].replace("/*" ,"ir")
        texto[i] = texto[i].replace("*/" ,"is")
        texto[i] = texto[i].replace("/*" ,"ir")
        texto[i] = texto[i].replace("//" ,"jt")
        texto[i] = texto[i].replace("++" ,"it")
        texto[i] = texto[i].replace("--" ,"iu")
        texto[i] = texto[i].replace("0", "")
        texto[i] = texto[i].replace("1", "")
        texto[i] = texto[i].replace("2", "")
        texto[i] = texto[i].replace("3", "")
        texto[i] = texto[i].replace("4", "")
        texto[i] = texto[i].replace("5", "")
        texto[i] = texto[i].replace("6", "")
        texto[i] = texto[i].replace("7", "")
        texto[i] = texto[i].replace("8", "")
        texto[i] = texto[i].replace("9", "")

    for i in range(len(texto)):
        x = texto[i]
        for c in x:
            k = c
            for j in range(len(tokens)):
                if(k == tokens[j][0]):
                    k = tokens[j][1]
            if(c != k):
                x = x.replace(c,k)
        texto[i] = x
    return texto

# passa como parametro um arquivo de tokens e o transforma em uma lista de tuplas
def token(arquivoToken): 
    fp = open(arquivoToken)
    tokens = fp.readlines()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace("\n", "")
        tokens[i] = tuple(tokens[i].split(' '))
    return tokens

#transforma todas as letras em minusculas
def minusculas(texto):
    texto = ''.join(texto)
    texto = texto.lower()
    return texto
    
#calcula as n-gramas dos tokens gerados
def calcNgram(listapalavras, n):
    ngrams = []
    vocabulario = []
    for i in range(len(listapalavras)-(n-1)):
        ngrams.append(listapalavras[i:i+n])
    for n, i in enumerate(ngrams):
        auxi = "".join(str(x) for x in i)
        vocabulario.append(auxi)
    return vocabulario

#insere em um dicionario o documento e os termos do vocabulario
def insereTermos(file, vocab_atual, colecao):
    key_file = file
    vocab_file = vocab_atual
    colecao.append({key_file: vocab_file})
    return colecao

#Nº de doc em q o termo ocorre na coleção
def preencheTermos(termos_colecao_c, list_c):
    termos_number = {}
    for i in termos_colecao_c:
        termos_number[i] = None
    for i in termos_number:
        cont = 0
        for j in list_c:
            for x in j.items():
                if i in x[1]:
                    cont +=1
                    termos_number[i] = cont
    return termos_number

#transforma a colecao de documentos em listas para o bm25 (obs: a execução se torna mais facil)
def emLista(docs_colecao):
    lista_colecao = []
    for i in docs_colecao:
        c = i
        for t in c.items():
            lista_colecao.append(t)
    return lista_colecao