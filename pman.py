from colorama import Fore, Back, Style, init
import getpass
import random
init(autoreset=True)
print("\033c",end="")

L=[]
i=False
while True:
    print(Fore.BLACK+"------WELCOME-------")
    print("\n\n")
    print(Fore.BLACK+"1]Registrati:       ")
    print(Fore.BLACK+"2]Accedi:           ")
    print(Fore.BLACK+"3]Visualizza Utenti:")
    print(Fore.BLACK+"4]Elimina utente:")
    print(Fore.BLACK+"5]Recupera password:")
    print(Fore.BLACK+"6]Esci:")
    print("\n\n")
    scelta = input(Fore.GREEN+"Cosa vuoi scegliere?: ")

    if scelta == "1":
        nick = input(Fore.YELLOW+"Inserisci un nickname: ")
        password = getpass.getpass(Fore.YELLOW+"Inserisci la tua password: ")
        email=input(Fore.YELLOW+"Inserisci la tua mail:")

        utente_presente = False
        for utente in L:
            if utente.get("nick") == nick:
                utente_presente = True
                break

        if utente_presente:
            print(Fore.BLUE+"Questo nickname è già stato utilizzato.")

            numero_casuale = random.randint(0, 100)
            nuovo_nick = str(nick)+str(numero_casuale)

            for utente in L:
                if utente.get("nick") == nuovo_nick :
                    numero_casuale = random.randint(0, 100)
                    nuovo_nick = str(nick)+str(numero_casuale)

            print(Fore.GREEN+"Hai ottenuto un nuovo nickname: ",nuovo_nick)
            nick = nuovo_nick

        utente = {
            "nick": nick,
            "password": password,
            "email": email,
        }
        L.append(utente)
        i=True
    elif scelta=="2":
        print("\033c",end="")
        if i==True:
            print("Login:")
            nick_log=input(Fore.YELLOW+"Inserisci il nome utente:")
            pass_log=getpass.getpass(Fore.YELLOW+"Inserisci la password")

            for utente in L:
                if utente["nick"]==nick_log and utente["password"]==pass_log:
                    print(Fore.GREEN+"Accesso effettuato con succeso")
                    #i=False
                    break
                else:
                    print(Fore.RED+"Nome utente o password errati")
                    #i=False
                    break
        else:
            print("Non ci sono utenti")
            
    elif scelta=="3":
        for utente in L:
            print(Fore.CYAN+"nick: ",utente["nick"],Fore.CYAN+"password: *********",Fore.CYAN+"email:",utente["email"])
    
    elif scelta=="4":
        tentativi=3
        while tentativi>0:
            nome=input(Fore.YELLOW+"Nome: ")
            rem_pass=getpass.getpass(Fore.YELLOW+"Inserire la password per rimuovere l'utente:")
            for utente in L:
            
                if utente["nick"]==nome and utente["password"]==rem_pass:
                    L.remove(utente)
                    tentativi=0
                    break
                else:
                    print(Fore.BLACK+"Nome utente o password errati, riprova")
                    print(Fore.BLACK+"Ti restano:",tentativi-1,Fore.BLACK+" tentativi")
                    tentativi-=1
    elif scelta=="5":
        rec_nick=input(Fore.YELLOW+"Inserisci il tuo nickname:")
        rec_email=input(Fore.YELLOW+"Inserisci la tua mail:")
        for utente in L:
            if utente["nick"]==rec_nick and utente["email"]==rec_email:
                new_pass=getpass.getpass(Fore.YELLOW+"Inserisci la nuova password")
                utente["password"]=new_pass
                break
            else:
                print(Fore.RED+"Credenziali errate")
                break

    elif scelta=="6":
        break

print("\033c",end="")
print(Fore.WHITE+"Arrivederci")

