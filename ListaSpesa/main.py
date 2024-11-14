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

def conteggio():
    cont =0 
    for i in range(len(lista)):
        cont += 1
    print(f"la lista contiene {cont} elementi")

def svuotaLista():
    for i in range(len(lista)):
        lista.remove(lista[i-1])

controllo = True
while controllo == True:
    print("------------------------------------")
    print("1) aggiungi un elemento alla lista")
    print("2) visualizza la lista")
    print("3) elimina un elemento dalla lista")
    print("4) numero di elementi contenuti nella lista")
    print("5) svuota la lista")
    x = input("inserisci il numero dell'azione che vuoi eserguire:")
    if x == "1":
        aggiunta()
    elif x== "2":
        stampaLista()
    elif x=="3":
        eliminaElemento()
    elif x== "4":
        conteggio()
    elif x== "5":
        svuotaLista()
    else:
        uscita= input("vuoi uscire? (y/n)")
        uscita.lower()
        if uscita == "y":
            controllo = False
        
