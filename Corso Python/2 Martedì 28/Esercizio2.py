#Chiedere l'età
età = int(input("Qual'è la tua età?"))

if(età < 18):
    print("non puoi vedere questi film")
    exit()
else:
    print("scegli il film da vedere")

#scegliere il film da vedere
film = ["It 2", "Paranormal Activity", "La Bambola Assassina"]

film_da_vedere = input("Scegli il film 1, 2 o 3 ")

if film_da_vedere == "1":
    print("hai scelto di vedere It 2")
elif film_da_vedere == "2":
    print("hai scelto di vedere Paranormal Activity")
elif film_da_vedere == "3":
    print("hai scelto di vedere La bambola assassina")
else:
    print("arrivederci")
