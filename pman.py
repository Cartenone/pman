from colorama import Fore, Back, Style, init
import getpass
import random
import menu
init(autoreset=True)
print("\033c",end="")

L=[]


i=False
def main():
    init(autoreset=True)
    menu.clear_screen()
    L = []
    i = False

    while True:
        menu.welcome_menu()
        scelta = input(Fore.GREEN+"Cosa vuoi scegliere?: ")

        if scelta == "1":
            menu.register_user(L)
            i = True
        elif scelta == "2":
            menu.login_user(L)
        elif scelta == "3":
            menu.display_users(L)
        elif scelta == "4":
            menu.delete_user(L)
        elif scelta == "5":
            menu.recover_password(L)
        elif scelta == "6":
            break

    menu.clear_screen()
    print(Fore.WHITE+"Arrivederci")

if __name__ == "__main__":
    main()