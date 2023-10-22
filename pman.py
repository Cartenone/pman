from colorama import Fore, Back, Style, init
import getpass
import random
init(autoreset=True)
print("\033c",end="")

L=[]
while True:
    print("------WELCOME-------")
    print("\n\n")
    print("1]Registrati:       ")
    print("2]Accedi:           ")
    print("3]Visualizza Utenti:")
    print("4]Elimina utente:")
    print("5]Esci:")
    print("\n\n")
    scelta = input("Cosa vuoi scegliere?: ")

    if scelta == "1":
        nick = input("Inserisci un nickname: ")
        password = getpass.getpass("Inserisci la tua password: ")

        utente_presente = False
        for utente in L:
            if utente.get("nick") == nick:
                utente_presente = True
                break

        if utente_presente:
            print("Questo nickname è già stato utilizzato.")

            numero_casuale = random.randint(0, 100)
            nuovo_nick = str(nick)+str(numero_casuale)

            for utente in L:
                if utente.get("nick") == nuovo_nick :
                    numero_casuale = random.randint(0, 100)
                    nuovo_nick = str(nick)+str(numero_casuale)

            print("Hai ottenuto un nuovo nickname: ",nuovo_nick)
            nick = nuovo_nick

        utente = {
            "nick": nick,
            "password": password,
        }
        L.append(utente)
    elif scelta=="2":
        print("\033c",end="")
        print("Login:")
        nick_log=input("Inserisci il nome utente:")
        pass_log=getpass.getpass("Inserisci la password")

        for utente in L:
            if utente["nick"]==nick_log and utente["password"]==pass_log:
                print("Accesso effettuato con succeso")
            else:
                print("Nome utente o password errati")
        
    elif scelta=="3":
        for utente in L:
            print("nick: ",utente["nick"],"password: *********")
    
    elif scelta=="4":
        tentativi=3
        while tentativi>0:
            nome=input("Nome: ")
            rem_pass=getpass.getpass("Inserire la password per rimuovere l'utente:")
            for utente in L:
            
                if utente["nick"]==nome and utente["password"]==rem_pass:
                    L.remove(utente)
                    tentativi=0
                    break
                else:
                    print("Nome utente o password errati, riprova")
                    print("Ti restano:",tentativi-1," tentativi")
                    tentativi-=1
    
    elif scelta=="5":
        break

print("\033c",end="")
print("Arrivederci")

