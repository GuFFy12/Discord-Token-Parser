import colorama, os, ctypes, re
from colorama import Fore, init
from sys import exit

os.system("cls")
if __name__ == '__main__':
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Discord Token Checker by GuFFy_OwO")
    colorama.init()

print(f"{Fore.MAGENTA}Discord Token Parser by GuFFy_OwO\n")
tokenFileName = input(f"{Fore.GREEN}Enter the name of the file in wich are the unchecked tokens (without .txt) : ")
deleteDuplicates = input(f"{Fore.GREEN}Delete duplicates tokens? [Y/N] : ")

if (not os.path.exists(tokenFileName + ".txt")):
    print(tokenFileName + ".txt" + " not exist.")
    input(f"{Fore.MAGENTA}Press Enter button for exit")
    exit()

def main():
    try:
        os.remove("Parsed Tokens.txt")
    except: None
    open("Parsed Tokens.txt", 'a+')
    tokens = []
    for line in [x.strip() for x in open(f'{tokenFileName}.txt', errors='ignore').readlines() if x.strip()]:
        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
            for token in re.findall(regex, line):
                tokens.append(token)
    if deleteDuplicates.lower() == "y":
        tokens = list(dict.fromkeys(tokens))
    tokens_str = '\n'.join(tokens)
    with open("Parsed Tokens.txt", "a", encoding='utf-8') as f:
        f.write(tokens_str)
    found = sum(1 for line in open("Parsed Tokens.txt", 'r', encoding='utf-8')) 
    print(f"{Fore.CYAN}\nDone. Found {found} tokens!\n")
    input(f"{Fore.MAGENTA}Press Enter button for exit")
    exit()
      
main()
