def magia():
    file = open('sexo.txt', "r")
    numeros = file.readlines()
    file.close()
    return numeros

def sexogostoso(numeros):
    for i in numeros:
        print(i)

def sexosemconsentimento(numeros):
    cardapio = []
    ALBERIS = 0
    for i in numeros:
        if i != '\n':
            SandroCurio = int(i.replace("\n", ""))
            ALBERIS +=  SandroCurio
        if i == '\n':
            cardapio.append(ALBERIS)
            ALBERIS = 0
    return cardapio  

def SEXOAGOSTO(numeros):
    Bailão = []
    for i in numeros:
        Sexãogostoso = max(numeros)
        Bailão.append(Sexãogostoso)
        numeros.remove(Sexãogostoso)
    return Bailão        

Amizade = sexosemconsentimento(magia())
COPULAÇÃO = max(Amizade)
Verdade = SEXOAGOSTO(Amizade)
TRANSA = Verdade[0] + Verdade[1] + Verdade[2]

print(COPULAÇÃO)
print(TRANSA)




