
while True:
    try:
        a = int(input("Inserisci un intero: "))
        break
    except ValueError:
        print("Input non valido, riprova")

print(f"Hai inserito: {a}")