totalAbono = 0
funcionarioTotal = 0
maiorAbono = 0
minimoAbono = 0


while True:
    salario = float (input("\nDigite o salario (Aperte 0 e de enter para cancelar!): "))
    if salario == 0: 
        break
    else:   
        abono = salario * 0.2
        if abono < 100 and abono >0:
            abono = 100

        funcionarioTotal += 1

        totalAbono = totalAbono + abono
        if abono == 100:
            minimoAbono += 1
        
        if abono > maiorAbono:
            maiorAbono = abono

        print ('Salario - Abono ')
        print("R$", salario, "- R$",abono, "\n")

print("\n\nProjeção de Gastos com Abono")
print("============================")
print("\nForam processados", funcionarioTotal, "colaboradores")
print("Total gasto com abono: R$", totalAbono)
print("Valor mínimo pago a", minimoAbono, "colaboradores" )
print("Maior valor de abono pago: R$", maiorAbono, "\n\n")