SemaforoVerde = input("Il semaforo è verde? (True/False): ")
if SemaforoVerde == "True":
    SemaforoGiallo = input("Il semaforo è giallo? (True/False): ")
    if SemaforoGiallo == "False":
        SemaforoRosso = input("Il semaforo è rosso? (True/False): ")
        if SemaforoRosso == "False":
            print("Puoi passare.")
        else:
            print("Fermati.")
    else:
        print("Inizia a fermarti.")
else:
    print("Fermati.")


