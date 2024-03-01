print("Este programa analisa os valores digitados de 0 à 6 e diz o dia da semana")
digito = input("Entre com um número de 0 à 6: ")

match digito:
    case '0' | '10':
        print("Domingo")
    case '1':
        print("Segunda-Feira")
    case '2':
        print("Terça-Feira")
    case '3':
        print("Quarta-Feira")
    case '4':
        print("Quinta-Feira")
    case '5':
        print("Sexta-Feira")
    case '6':
        print("Sábado")
    case _:
        print("Valor incorreto. Tente outra vez")
        