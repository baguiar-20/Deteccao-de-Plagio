for fruta in [ "banana", "maca ", "uva" ]:
    print ("Fruta : " + fruta)
    print("------------------------------")
for i in range (0,10): #(Inclui o Zero, NÃO INCLUI O 10)
    print ("i = " + str ( i ))
    print("------------------------------")
    for i in range(0,10):
        print ('Não realizado1')
        if i == 0:
            break
    print('Realizado')