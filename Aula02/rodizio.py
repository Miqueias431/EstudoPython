print("Este programa analisa os valores digitados de 0 à 9 e diz o dia da semana que você não pode rodar com o carro")
digito = input("Digite o final da placa: ")

match digito:
    case '1' | '2':
        print("Seu carro não pode rodar na Segunda-Feira")
    case '3' | '4':
        print("Seu carro não pode rodar na Terça-Feira")
    case '5' | '6':
        print("Seu carro não pode rodar na Quarta-Feira")
    case '7' | '8':
        print("Seu carro não pode rodar na Quinta-Feira")
    case '9 | 0':
        print("Seu carro não pode rodar na Sexta-Feira")
    case _:
        print("Valor incorreto. Tente outra vez")
        