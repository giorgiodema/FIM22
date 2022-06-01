
while True:
    # utilizzo le clausole try/except per gestire un input 
    # sbagliato da parte dell'utente
    try:
        a = int(input("Inserisci un intero: "))
        break
    except ValueError:
        print("Input non valido, riprova")

print(f"Hai inserito: {a}")