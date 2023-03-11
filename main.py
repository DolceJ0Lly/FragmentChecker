#   By GodAlecs

#   GitHub: github.com/GodALecs/FragmentChecker

#   Libs

import requests

import os

import platform

from colorama import Fore

#   Variables

saves = "saves.txt" # Variable of the file Saves.txt

link = "https://fragment.com/username/" # Link fragment

banner = f"""

{Fore.RED}▄████  █▄▄▄▄ ██     ▄▀  █▀▄▀█ ▄███▄      ▄     ▄▄▄▄▀ 

█▀   ▀ █  ▄▀ █ █  ▄▀    █ █ █ █▀   ▀      █ ▀▀▀ █    

█▀▀    █▀▀▌  █▄▄█ █ ▀▄  █ ▄ █ ██▄▄    ██   █    █    

█      █  █  █  █ █   █ █   █ █▄   ▄▀ █ █  █   █     

█       █      █  ███     █  ▀███▀   █  █ █  ▀      

▀     ▀      █          ▀           █   ██         

            ▀                                      

{Fore.YELLOW}▄█▄     ▄  █ ▄███▄   ▄█▄    █  █▀ ▄███▄   █▄▄▄▄      

█▀ ▀▄  █   █ █▀   ▀  █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀      

█   ▀  ██▀▀█ ██▄▄    █   ▀  █▀▄   ██▄▄    █▀▀▌       

█▄  ▄▀ █   █ █▄   ▄▀ █▄  ▄▀ █  █  █▄   ▄▀ █  █       

▀███▀     █  ▀███▀   ▀███▀    █   ▀███▀     █        

        ▀                   ▀             ▀     

        

    {Fore.RED}github.com/GodAlecs/FragmentChecker

    """ #   Banner

#   Funzione check_user

def check_user(username): 

    username = username.strip()

    r = requests.get(f"https://fragment.com/username/{username}", allow_redirects=False) #  Check if the user is on shop

    response = str(r.text).split('\n')

    if len(response) != 1:

        print(f"{Fore.GREEN}[+]{Fore.RESET} {username} can be buy it on Fragment.com")

    else:

        print(f"{Fore.RED}[-]{Fore.RESET} {username} can't be buy on fragment.com")

        #   Down saves the username the can't be buyed

        saves_file = open(saves, "a")

        saves_file.write(f"[-] {username}\n")

        saves_file.close()

#   Function Main

def main():

    if "linux" in str(platform.platform()).lower(): # Wash the screen (remove the writing)

        os.system("clear")

    else: 

        os.system("cls")

    print(banner)

    wordlist = input(f"{Fore.RESET}[>>] Enter the name of the file of the  {Fore.GREEN}wordlist{Fore.RESET} -> ") #  Enter the name

    try: #  Check if exist the file...

        wordlist_file = open(wordlist, "r")

        print(f"{Fore.RESET}[>>] File {wordlist} {Fore.GREEN}Loaded!{Fore.RESET}!")

        try: #  Check if the file is exist for the name can't buy on fragment.com

            saves_file = open(saves, "r+")

            print(f"{Fore.RESET}[>>] File {saves} {Fore.GREEN}Loaded!{Fore.RESET}!")

            saves_file.truncate(0) #    Delete all data

            saves_file.close() #   Close the file Saves.txt

            pass

        except FileNotFoundError: # Create file saves.txt

            saves_file = open(saves, "w")

            print(f"{Fore.RESET}[>>] File {saves} {Fore.GREEN}Crated{Fore.RESET}!")

            saves_file.close()

    except FileNotFoundError: # File wordlist not found

        print(f"{Fore.RESET}[>>] File {wordlist} {Fore.RED}Not found{Fore.RESET}!")

        exit() #    Finish the program

    print() #   Blank Space

    for username in wordlist_file.readlines():

        check_user(username.lower())

if __name__ == "__main__":

    main() #    Recall Class 
