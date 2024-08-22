import math

def calcola_perimetro_quadrato(lato):
    return lato * 4

def calcola_perimetro_cerchio(raggio):
    return 2 * math.pi * raggio

def calcola_perimetro_rettangolo(base, altezza):
    return (base * 2) + (altezza * 2)

def calcola_perimetro_triangoloIsoscele(base, latoisoscele):
    return base + (latoisoscele * 2)


def main():
    print("Scegli una figura geometrica per calcolare il perimetro: ")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    print("4. Triangolo Isoscele")
    
    scelta = input("Inserisci il numero della tua scelta 1-2-3-4: ")

    if scelta == '1':
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = calcola_perimetro_quadrato(lato)
        print(f"Il perimetro del quadrato è: {perimetro}")

    elif scelta == '2':
        raggio = float(input("Inserisci il raggio del cerchio: "))
        perimetro = calcola_perimetro_cerchio(raggio)
        print(f"La circonferenza del cerchio è: {perimetro}")

    elif scelta == '3':
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = calcola_perimetro_rettangolo(base, altezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")
    
    elif scelta == '4':
        base = float(input("Inserisci la lunghezza della base delò triangolo: "))
        latoisoscele = float(input("inserisci la lunghezza del lato isoscele"))
        perimetro = calcola_perimetro_triangoloIsoscele(base, latoisoscele)
        print(f"il perimetro del triangolo è: {perimetro}")

    else:
        print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()