
numPrimo = float(input("Insira um número para a verificação de primo: "))

if(numPrimo == 2 or numPrimo == 3 or numPrimo == 5 or numPrimo == 7 ):
    print(numPrimo, " é primo")
elif(numPrimo % 2 == 0 or numPrimo % 3 == 0 or numPrimo % 5 == 0 or numPrimo % 7 == 0 ):
    print(numPrimo, " não é primo")
else:
    print(numPrimo, "é Primo")