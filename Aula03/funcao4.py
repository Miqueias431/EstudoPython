# Criar uma função que escreva a tabuada para um
# determinado valor definido pelo usuário em
# um arquivo de texto

def tabuada(numero, arquivo):
    f = open(arquivo, 'w')
    f.write(f"Tabuada do {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        f.write(f"{numero} x {i} = {resultado}\n")
    f.close()

def main():
    numero = int(input("Digite um número para gerar a tabuada: "))
    nome_arquivo = input("Digite o nome do arquivo para salvar a tabuada (ex: tabuada.txt): ")

    tabuada(numero, nome_arquivo)
    print(f"Tabuada do {numero} foi gerada e salva em {nome_arquivo} com sucesso!")

main()
