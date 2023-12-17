def cal():
    operadores = (1, 2, 3, 4)
    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))
    op = ''' 
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair '''
    print(f"Digite o operador, sendo eles {op}")
    operador = int(input())
    operacao_inexistente = (operador not in operadores) and (operador != 0)
    if operacao_inexistente:
        print("Essa opção não existe")
        return True
    elif operador == 0:
        print("Fim do programa")
        return False
    elif operador == 1:
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
        return True
    elif operador == 2:
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
        return True
    elif operador == 3:
        print(f"{num_1} x {num_2} = {num_1 * num_2}")
        return True
    elif operador == 4:
        print(f"{num_1} ÷ {num_2} = {num_1 // num_2}")
        return True
    
while True:
    resposta = cal()
    if not resposta:
        break