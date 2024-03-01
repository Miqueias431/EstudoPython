# Estudo Python 
<img src="https://ictslab.com/wp-content/uploads/2019/03/d1326ca6cca8038cd115a061b4e2b3bc-840x430.png"  width="400" height="200">

## Aula 01

### Arquivo mensagem.py

```py
print("Olá, eu sou um arquivo escrito em Python")
```

### Arquivo boasvindas.py

```py
# Vamos criar uma variave para armazenar o
# nome do usuário
nome = "admin"
print("Olá, "+nome+". Seja bem vindo!")
print("Escreva o seu novo nome de usuário.")
nome = input("Digite aqui:")
print("O seu novo usuário é: "+nome)
```

### Arquivo desvioif.py

```py
# Pede um número e verifica se é par ou impar
numero = input("Digite um número: ")
# É necessário realizar a conversão de texto para
# número, pois a função input sempre retorna o valor
# em formato texto. Então, utilizamos a função
# int para converter a variável numero em valor
# numérico inteiro e assim realizar os cálculos
# necessários.
numero = int(numero)

if(numero % 2 == 0):
    print("O número digitado é Par")
else:
    print("O número digitado é Impar")
```
### Arquivo desvioif2.py

```py
n1 = input("Digite a primeira nota do aluno: ")
n2 = input("Digite a segunda nota do aluno:  ")
n3 = input("Digite a terceira nota do aluno: ")
n4 = input("Digite a quarta nota do aluno:   ")
rs = (int(n1)+int(n2)+int(n3)+int(n4)) / 4
# Se o aluno tiver uma média acima ou igual a 7,
# então estará APROVADO. Senão se a média
# for abaixo ou igual a 4, estão estará REPROVADO
# caso contrário, estará em RECUPERAÇÃO
print("Sua média é: "+str(rs)+", então você está:" )
if( rs >= 7 ):
    print("Aprovado")
elif( rs <= 4 ):
    print("Reprovado")
else:
    print("Recuperação")
```

## Aula 02

### Arquivo match1.py

```py
print("Este programa analisa os valores digitados de 0 à 6 e diz o dia da semana")
digito = input("Entre com um número de 0 à 6: ")

match digito:
    case '0':
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
        
```