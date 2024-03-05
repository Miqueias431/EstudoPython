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

```

### Arquivo rodizio.py

```py 
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

```

### Arquivo for1.py

```py
# Para realizar a contagem de  1 até 10 é necessario 
# fazer uso de uma estrutura chamada range e 
# citar os valores 1 até 11. O range nunca conta
# o valor de parada, Neste caso o valor 11

for i in range(1,11):
    print(i)

```

### Arquivo for2.py

```py
# faça uma contagem de um até 300 exibindo apenas
# os números multiplos de 4

for i in range(1,301):
    if (i % 4 == 0):
        print(i)

```

### Arquivo for3.py

```py
n = [1,54,12,63,74,13,9,25,7,32]
for i in n:
    print(i)

```

### Arquivo calculo_cpf.py

```py
print("Programa que verifica se o CPF é válido")


# Variável que guarda o CPF digitado pelo usuário.
cpf_usuario =input("Digite o seu CPF:")


# Criar uma variável para guadar o CPF que estamos 
# calculando
cpf_calc = ""


# Esta variável foi criada para calcular o peso 
# de 10 até 2.
peso10 = 10
peso11 = 11

# A variável resultada guarda a soma das multiplicações
# entre as digitos do CPF e os pesos.
resultado = 0


# Para obter os 9 primeiros digitos do CPF foi necessário
# usar um estrutura for com uma contagem de 0 até 9.
for i in range(0,9):
    
    
    # Exibindo um digito do CPF por vez em tela.
    print(cpf_usuario[i])
    
    
    # Adicionar a variável cpf_calc os nove primeiros
    # digitos do cpf e add o primeiro digito
    # verificador mais adiante
    cpf_calc += cpf_usuario[i]
    
    
    print(int(cpf_usuario[i])*peso10)
    # Para calcular um digito por vez com o peso foi
    # necessário converter cada digito em número inteiro
    # depois, somamos os resultados obtidos armazenando
    # na variável resultado.
    resultado+=int(cpf_usuario[i])*peso10
    # Todas as vezes que o laço for rodar, será subtraido
    # o valor 1 da variável peso10.
    peso10-=1
    
    
# Exibindo o resultado enconntrado.
print(resultado)


# A variável resto guarda o resto da divisão.
resto = resultado % 11


# Se o resto da divisão for menor que 2, então o
# primeiro digito será 0(zero); Caso contrário o
# devemos subtrair 11 pelo valor encontrado em resto.
if(resto < 2 ):
    print("Primeiro digito é 0")
    cpf_calc+="0"
else:
    print("Primeiro digito é: "+str(11-resto))
    cpf_calc+=str(11-resto)
    
    
resultado = 0


for i in range (0,10):
    resultado+=int(cpf_calc[i]*peso11)
    
resto = resultado % 11

if(resto < 2 ):
    cpf_calc+="0"
else:
    
    cpf_calc+=str(11-resto)
    
    

print(cpf_calc)
# Validar se o CPF do usuário é igual ao CPF calculado

if(cpf_usuario==cpf_calc):
    print("CPF é Válido")
else:
    print("CPF inválido")
    
```