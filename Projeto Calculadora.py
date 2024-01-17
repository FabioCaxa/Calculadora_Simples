import os

print("Bem vindo a Calculadora")
print("=======================")

while True:
    print("Por favor, escolha um número para o tipo de operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    operacao = input()

    try:
        operacao = int(operacao)
    except ValueError:
        print("Valor incorreto, por favor utilize os números de 1 a 4")
        continue

    if operacao not in [1, 2, 3, 4]:
        print("Valor incorreto, por favor utilize os números de 1 a 4")
        continue

    os.system('cls' if os.name == 'nt' else 'clear')
    if operacao == 1:
        print("1 - Soma")
    elif operacao == 2:
        print("2 - Subtração")
    elif operacao == 3:
        print("3 - Multiplicação")
    else:
        print("4 - Divisão")

    try:
        primeiro = float(input("Por favor, insira o primeiro número: "))
        segundo = float(input("Por favor, insira o segundo número: "))
    except ValueError:
        print("Valores incorretos. Por favor, insira números válidos.")
        continue

    if operacao == 1:
        resultado = primeiro + segundo
        print(f"{primeiro} + {segundo} = {resultado}")
    elif operacao == 2:
        resultado = primeiro - segundo
        print(f"{primeiro} - {segundo} = {resultado}")
    elif operacao == 3:
        resultado = primeiro * segundo
        print(f"{primeiro} * {segundo} = {resultado}")
    elif operacao == 4:
        if segundo == 0:
            print("Divisão por zero não permitida.")
            continue
        else:
            resultado = primeiro / segundo
            print(f"{primeiro} / {segundo} = {resultado:.2f}")
    else:
        print("Valor incorreto, por favor utilize os números de 1 a 4")

    outra = input("Gostaria de fazer outra operação? (s/n): ")

    if outra.lower() == "s" or outra.lower() == "sim":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif outra.lower() == "n" or outra.lower() == "nao" or outra.lower() == "não":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Obrigado por usar a Calculadora!")
        break
    else:
        print("Valor incorreto. Utilize s ou n.")
