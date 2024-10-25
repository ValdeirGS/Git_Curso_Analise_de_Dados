def calcular_inss(salario_bruto):

    if salario_bruto <= 1412:
        inss = salario_bruto * 0.075
    elif salario_bruto > 1412 and salario_bruto <= 2666.68:
        inss = salario_bruto * 0.09 - 21.18
    elif salario_bruto > 2666.68 and salario_bruto <= 4000.03:
        inss = salario_bruto * 0.12 - 101.18
    else:
        inss = salario_bruto * 0.14 - 181.18
    
    return round(inss, 2)

def calcular_ir(salario_bruto):
    
    inss = calcular_inss(salario_bruto)
    salario_descontado = salario_bruto - inss
    
    if salario_descontado <= 2259.20:
        ir = 0
    elif salario_descontado > 2259.20 and salario_descontado <= 2826.65:
        ir = salario_descontado * 0.075 - 169.44
    elif salario_descontado > 2826.65 and salario_descontado <= 3751.05:
        ir = salario_descontado * 0.15 - 381.44
    elif salario_descontado > 3751.05 and salario_descontado <= 4664.68:
        ir = salario_descontado * 0.225 - 662.77
    else:
        ir = salario_descontado * 0.275 - 896
    return round(ir, 2)


def verificar_estoque(saldo, estoque_min, estoque_max):
    if saldo > estoque_max:
        reposicao = 0
    elif saldo < estoque_max:
        reposicao = estoque_max - saldo
    elif saldo == 0:
        reposicao = estoque_max - saldo
    else:
        reposicao = 0
    
    matriz = [[saldo, estoque_min, estoque_max, reposicao]]
    return matriz

# Primeiro, capturar os dados do usuário
saldo = float(input("Digite o saldo: "))
estoque_min = float(input("Digite o estoque mínimo: "))
estoque_max = float(input("Digite o estoque máximo: "))

# Depois, aplicar as condições com if
resultado = verificar_estoque(saldo, estoque_min, estoque_max)

# Lançamento dos dados
for linha in resultado:
    print("Saldo:", linha[0])
    print("Estoque Mínimo:", linha[1])
    print("Estoque Máximo:", linha[2])
    print("Reposição:", linha[3])  # Caractere não imprimível removido
