print("Programa que verifica se o CPF é válido")
# Variável que guarda o CPF digitado pelo usuário.
cpf_usuario =input("Digite o seu CPF:")
# Esta variável foi criada para calcular o peso 
# de 10 até 2.
peso10 = 10

# A variável resultada guarda a soma das multiplicações
# entre as digitos do CPF e os pesos.
resultado = 0

# Para obter os 9 primeiros digitos do CPF foi necessário
# usar um estrutura for com uma contagem de 0 até 9.
for i in range(0,9):
    # Exibindo um digito do CPF por vez em tela.
    print(cpf_usuario[i])
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
else:
    print("Primeiro digito é: "+str(11-resto))
    