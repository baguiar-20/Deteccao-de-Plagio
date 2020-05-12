var1 = int(input("Digite um Número para var1"))
var2 = int(input("Digite um Número para var2"))
if var1 == 1:
  print("Número var1 igual a 1")
elif var1 == 2 or var2 == 3:
  print("var1 diferente de 1 ou var2 diferente de 2")
elif var1 >= 1000 or var2 <= -1000:
  print("var1 maior que 1000 ou var2 menor que -1000")
else:
  print("nenhuma das alternativas anteriores")