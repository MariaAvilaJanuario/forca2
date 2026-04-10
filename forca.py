import random
print ("-- JOGO DA FORCA --")

with open("palavras.txt") as f:
    conteudo = f.read()
    palavras = conteudo.splitlines()
    escolhida = random.choice(palavras)

secreta = [ ]

for x in escolhida:
    secreta.append("_")
print( )
for x in secreta:
    print(x, end = ' ')
print ( )

while (secreta != escolhida):
    y = 0
    while (y < 10):
        chute = str(input("Digite uma letra: "))
        if (chute in escolhida):
            print (chute, " existe na palavra")
            print ( )
        
            for i in range(0,len(escolhida)):
                if escolhida[i] == chute:
                    secreta[i] = chute
        
            for x in secreta:
                print(x, end = ' ')
            print ( )

        elif (chute not in escolhida):
            print (chute, " não existe na palavra")
            y = y + 1
            print( )
            letras.append(chute)

        if (y == 10):
            print ("Forca! Você perdeu")
            print ("A palavra era" ,escolhida)

    if "_" not in secreta
        print ("Você acertou, parabéns")
        break