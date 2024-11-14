lista = []

def aggiunta():
    item = input("inserisci un elemento alla lista:")
    item.lower()
    lista.append(item)

def stampaLista():
    print(lista)

def eliminaElemento():
    print(lista)
    risp = input("inserisci il nome dell'elemento che vuoi eliminare")
    risp.lower()
    lista.remove(risp)

controllo = True
while controllo == True:
    print("1) aggiungi un elemento alla lista")
    print("2) visualizza la lista")
    print("3) elimina un elemento dalla lista")
    x = input("inserisci il numero dell'azione che vuoi eserguire:")
    if x == "1":
        aggiunta()
    elif x== "2":
        stampaLista()
    elif x=="3":
        eliminaElemento()
    else:
        uscita= input("vuoi uscire? (y/n)")
        uscita.lower()
        if uscita == "y":
            controllo = False
        
