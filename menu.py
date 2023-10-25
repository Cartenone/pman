from colorama import Fore, Back, Style, init
import getpass
import random

def clear_screen():
    print("\033c", end="")

def welcome_menu():
    print(Fore.BLACK+"------WELCOME-------")
    print("\n\n")
    print(Fore.BLACK+"1]Registrati:       ")
    print(Fore.BLACK+"2]Accedi:           ")
    print(Fore.BLACK+"3]Visualizza Utenti:")
    print(Fore.BLACK+"4]Elimina utente:")
    print(Fore.BLACK+"5]Recupera password:")
    print(Fore.BLACK+"6]Esci:")
    print("\n\n")

def register_user(L):
    nick = input(Fore.YELLOW+"Inserisci un nickname: ")
    password = getpass.getpass(Fore.YELLOW+"Inserisci la tua password: ")
    email = input(Fore.YELLOW+"Inserisci la tua mail:")

    utente_presente = False
    id_presente=False
    
    id_presente = False

# Genera un ID unico per l'utente
    id_utente = random.choice("abcdefghijklmnopqrstuvwxyz") + str(random.randint(0, 100))

    for utente in L:
        if utente["id_utente"] == id_utente:
            id_presente = True
            break

    if id_presente:
        print(Fore.BLUE + "Questo ID è già stato utilizzato.")
        id_casuale = random.choice("abcdefghijklmnopqrstuvwxyz") + str(random.randint(0, 100))
        nuovo_id = id_utente + id_casuale

        for utente in L:
            if utente["id_utente"] == nuovo_id:
                id_casuale = random.randint(0, 100)
                nuovo_id = id_utente + str(id_casuale)
        print(Fore.GREEN + "Hai ottenuto un nuovo ID: ", nuovo_id)
        id_utente = nuovo_id


    for utente in L:
        if utente.get("nick") == nick:
            utente_presente = True
            break

    if utente_presente:
        print(Fore.BLUE+"Questo nickname è già stato utilizzato.")
        numero_casuale = random.randint(0, 100)
        nuovo_nick = str(nick) + str(numero_casuale)

        for utente in L:
            if utente.get("nick") == nuovo_nick:
                numero_casuale = random.randint(0, 100)
                nuovo_nick = str(nick) + str(numero_casuale)

        print(Fore.GREEN+"Hai ottenuto un nuovo nickname: ", nuovo_nick)
        utente["nick"] = nuovo_nick

    utente = {
        "nick": nick,
        "password": password,
        "email": email,
        "id_utente": id_utente,
    }
    L.append(utente)

def login_user(L):
    if not L:
        print("Non ci sono utenti")
        return

    print("\033c", end="")
    print("Login:")
    nick_log = input(Fore.YELLOW+"Inserisci il nome utente:")
    pass_log = getpass.getpass(Fore.YELLOW+"Inserisci la password")

    for utente in L:
        if utente["nick"] == nick_log and utente["password"] == pass_log:
            print(Fore.GREEN+"Accesso effettuato con successo")
            return

    print(Fore.RED+"Nome utente o password errati")

def display_users(L):
    for utente in L:
        print(Fore.CYAN+"nick: ", utente["nick"], Fore.CYAN+"password: *********", Fore.CYAN+"email:", utente["email"],Fore.CYAN+"ID:",utente["id_utente"])

def delete_user(L):
    if not L:
        print("Non ci sono utenti")
        return

    tentativi = 3
    while tentativi > 0:
        scelta2=input("Vuoi eliminare per ID o per utente?:").upper()
        if scelta2=="UTENTE":
            nome = input(Fore.YELLOW+"Nome: ")
            rem_pass = getpass.getpass(Fore.YELLOW+"Inserire la password per rimuovere l'utente:")
            for utente in L:
                if utente["nick"] == nome and utente["password"] == rem_pass:
                    L.remove(utente)
                    tentativi=0
                    return print("Rimosso con successo!")
                else:
                    print(Fore.BLACK+"Nome utente o password errati, riprova")
                    print(Fore.BLACK+"Ti restano:", tentativi-1, Fore.BLACK+" tentativi")
                    tentativi -= 1
                    
        elif scelta2=="ID":
            nome = input(Fore.YELLOW+"ID: ")
            rem_pass = getpass.getpass(Fore.YELLOW+"Inserire la password per rimuovere l'utente:")
            for utente in L:
                if utente["id_utente"] == nome and utente["password"] == rem_pass:
                    L.remove(utente)
                    tentativi=0
                    return print("Rimosso con successo!")
                      
                else:
                    print(Fore.BLACK+"ID o password errati, riprova")
                    print(Fore.BLACK+"Ti restano:", tentativi-1, Fore.BLACK+" tentativi")
                    tentativi -= 1


def recover_password(L):
    rec_nick = input(Fore.YELLOW+"Inserisci il tuo nickname:")
    rec_email = input(Fore.YELLOW+"Inserisci la tua mail:")
    for utente in L:
        if utente["nick"] == rec_nick and utente["email"] == rec_email:
            new_pass = getpass.getpass(Fore.YELLOW+"Inserisci la nuova password")
            utente["password"] = new_pass
            return
    print(Fore.RED+"Credenziali errate")

