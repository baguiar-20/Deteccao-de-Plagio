import re


"""
    Módulo com funções que realizam o pré processamento e 
    e a substituição dos tokens no código
"""
#arquivos em c
#troca espaços vazios por token AB e remove comentarios e numeros
def removeEspacoC(texto):
    for i in range(len(texto)):
        texto[i] = texto[i].replace("\n", "")
        texto[i] = texto[i].replace("\\n", "")
        texto[i] = texto[i].replace(" ", "AB")
        texto[i] = texto[i].replace("\s", "")
        texto[i] = texto[i].replace("\t", "")        
    for i in range(len(texto)):
        x = texto[i]
        texto[i] = re.sub(r'//.*', '//', x) 
    return texto



#troca palavras reservadas da linguagem C para tokens (versao preguicosa)
def tokensC(texto):
    for i in range(len(texto)):
        texto[i] = texto[i].replace("unsigned", "hd")
        texto[i] = texto[i].replace("register" ,"gs")
        texto[i] = texto[i].replace("volatile", "hf")
        
        texto[i] = texto[i].replace("typedef", "hb")
        texto[i] = texto[i].replace("default" ,"gg")
        texto[i] = texto[i].replace("isalnum","hh")
        texto[i] = texto[i].replace("isalpha", "hi")
        texto[i] = texto[i].replace("isdigit", "hj")
        texto[i] = texto[i].replace("isspace", "hk")
        texto[i] = texto[i].replace("fprintf", "jj")
        texto[i] = texto[i].replace("sprintf", "jl")
        texto[i] = texto[i].replace("strncmp", "ij")
        texto[i] = texto[i].replace("scandir", "im")
        texto[i] = texto[i].replace("include" ,"ni")
        
        texto[i] = texto[i].replace("double", "gh")
        texto[i] = texto[i].replace("extern" ,"gl")
        texto[i] = texto[i].replace("signed", "gv")
        texto[i] = texto[i].replace("sizeof", "gx")
        texto[i] = texto[i].replace("static", "gw")
        texto[i] = texto[i].replace("struct", "gz")
        texto[i] = texto[i].replace("switch" ,"ha")
        texto[i] = texto[i].replace("fclose", "hs")
        texto[i] = texto[i].replace("getchar", "jn")
        texto[i] = texto[i].replace("printf", "jo")
        texto[i] = texto[i].replace("sscanf", "jq")
        texto[i] = texto[i].replace("getenv", "ib")
        texto[i] = texto[i].replace("malloc","id")
        texto[i] = texto[i].replace("strchr", "if")
        texto[i] = texto[i].replace("strcmp", "ig")
        texto[i] = texto[i].replace("strcpy", "ih")
        texto[i] = texto[i].replace("strlen", "ii")
        texto[i] = texto[i].replace("strstr", "ik")
        texto[i] = texto[i].replace("strtok", "il")
        texto[i] = texto[i].replace("sizeof", "in")
        texto[i] = texto[i].replace("typeof", "io")
        texto[i] = texto[i].replace("locale", "ja")
        texto[i] = texto[i].replace("stdlib", "jd")
        texto[i] = texto[i].replace("string", "je")
        texto[i] = texto[i].replace("clrscr", "og")
        texto[i] = texto[i].replace("return", "ci")
        
        
        texto[i] = texto[i].replace("const" ,"ge")
        texto[i] = texto[i].replace("union", "hc")
        texto[i] = texto[i].replace("floor", "hn")
        texto[i] = texto[i].replace("log10", "ho")
        texto[i] = texto[i].replace("fgetc", "jg")
        texto[i] = texto[i].replace("fgets", "jh")
        texto[i] = texto[i].replace("fopen", "ji")
        texto[i] = texto[i].replace("fputc", "jm")
        texto[i] = texto[i].replace("scanf", "jr")
        texto[i] = texto[i].replace("stdio", "jc")
        texto[i] = texto[i].replace("getch", "oe")
        texto[i] = texto[i].replace("conio", "of")
        
        texto[i] = texto[i].replace("auto" ,"ga")
        texto[i] = texto[i].replace("case" ,"gc")
        texto[i] = texto[i].replace("char" ,"gd")
        texto[i] = texto[i].replace("enum", "gk")
        texto[i] = texto[i].replace("goto", "go")
        texto[i] = texto[i].replace("long", "gr")
        texto[i] = texto[i].replace("void", "he")
        texto[i] = texto[i].replace("ceil", "hl")
        texto[i] = texto[i].replace("sqrt", "hr")
        texto[i] = texto[i].replace("feof", "ht")
        texto[i] = texto[i].replace("getc", "hu")
        texto[i] = texto[i].replace("gets", "hv")
        texto[i] = texto[i].replace("puts", "jp")
        texto[i] = texto[i].replace("atof", "hx")
        texto[i] = texto[i].replace("atoi", "hw")
        texto[i] = texto[i].replace("atol", "hz")
        texto[i] = texto[i].replace("free", "ic")
        texto[i] = texto[i].replace("rand", "ie")
        texto[i] = texto[i].replace("time", "jf")
        texto[i] = texto[i].replace("main", "od")

        texto[i] = texto[i].replace("exp", "hm")
        texto[i] = texto[i].replace("log", "hp")
        texto[i] = texto[i].replace("pow", "hq")
        texto[i] = texto[i].replace("int" ,"dw")
        texto[i] = texto[i].replace("for" ,"bv")

        texto[i] = texto[i].replace("do" ,"gi")   
        
    return texto
