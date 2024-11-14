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