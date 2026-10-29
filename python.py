from random import randint
while True:
    matriz=[]

    numeros=[]

    while True:
        linhas= int(input("A matriz deve ter quantas linhas?[Digite um número entre 2 e 10]"))
        if linhas > 10 or linhas < 2:
            print('Digite um número entre 2 e 10!')
            continue
        else:
            break


    while True:
        colunas= int(input("A matriz deve ter quantas colunas?[Digite um número entre 2 e 10]"))
        if colunas> 10 or colunas < 2:
            print("Digite um número entre 2 e 10!")
            continue
        else:
            break

    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            while True:
                num=randint(1,100)
                if num in numeros:
                    continue
                else:
                    numeros.append(num)
                    linha.append(num)
                    break
        matriz.append(linha)

    print("A matriz sorteada foi: ")

    for i in range(len(matriz)):
        print(matriz[i])


    while True:

        linha_sorteada = randint(0,linhas-1)
    
        coluna_sorteada = randint(0,colunas-1)
        
        print(f"Qual a linha e a coluna do número: {matriz[linha_sorteada][coluna_sorteada]} ?[lembre-se que o número da linha e da coluna começa por 0]")

        linha_inserir = int(input("Insira a linha: "))

        coluna_inserir = int(input("Insira a coluna: "))

        if linha_sorteada == linha_inserir and coluna_sorteada == coluna_inserir:
            print("Parábens!! Você acertou")
            break
        else:
            print(f"Você errou =(  A linha é {linha_sorteada} e a coluna é {coluna_sorteada}")
            flag01 = False
            while True:
                tentar = str(input("Quer tentar denovo com essa mesma matriz?[S/N]")).upper()
                if tentar == 'S':
                    break
                elif tentar == 'N':
                    flag01 = True
                    break
                else:
                    print("Digite S ou N!!")
                    continue
        if flag01:
            break

    while True:
        flag02 = False
        tentar02 = str(input("Quer jogar novamente com outra matriz?[Digite S ou N]")).upper()
        if tentar02 == "S":
            break
        elif tentar02 == "N":
            flag02 = True
            break
        else:
            print("Digite S ou N!!")
            continue
    if flag02:
        break

print("Obrigado por participar <3")




