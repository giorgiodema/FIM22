# La gestione delle eccezioni non deve essere
# usata per mascherare bug nel programma.
# Il seguente programma non è corretto in quanto la
# lista contiene 5 elementi e l'ultima iterazione del 
# ciclo accede al sesto elemento. Invece di gestire
# l'eccezione bisogna correggere il codice.

l = [1,2,3,4,5]

for i in range(6):
    # Uso sbagliato della gestione di
    # eccezioni
    try:
        print(f"l[{i}] = {l[i]}")
    except Exception:
        print("Something went wrong")

print("Program ended correctly")