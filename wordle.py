import random
lista=["silla", "pleno", "plano", "piano", "arena", "ajena", "anexa"]
palabra=random.choice(lista)
print(palabra)
respuesta="-----"
print(respuesta)
jugada=""
while(jugada!=palabra):
    acumulada=""
    print("Dime la palabra")
    jugada=input()
    for n in range(0, 5):
        encontrada=False
        for m in range(0, 5):        
            if(jugada[n]==palabra[m] and n==m):
                acumulada = acumulada + "*"
                encontrada=True
                break
        if(not encontrada):
            for m in range(0, 5):
                if (jugada[n]==palabra[m] and n!=m):
                    acumulada = acumulada + "+"
                    encontrada=True
                    break
        if(not encontrada):
            acumulada = acumulada + "-"
    print(acumulada)




