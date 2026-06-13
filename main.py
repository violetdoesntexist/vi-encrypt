import time
import art
from art import *
import colorama
from colorama import init, Fore, Back, Style
import random


alphabet = "abcdefghijklmnopqrstuvwxyzD"
alphnum = int(25)
Art = text2art("VIENCRYPT", chr_ignore=True)
print(Fore.MAGENTA + Art)

print(
    "what do you want to do? :)"
    "E = Encrypt"
    "D = Decrypt"
    "I = Project Info"
)

choice = input("choose:")
if(choice == "E"):
    encryption_key = input("enter key:")
    string = input("enter string:")
    while(alphnum > -1 ):
        decrypted = string.replace(encryption_key[alphnum], alphabet[alphnum] )
        print("replaced" + encryption_key[alphnum] + "with" + alphabet[alphnum] + decrypted)
        alphnum = alphnum - 1
        time.sleep(0.5)

    print("string" + string + "encrypted with key" + encryption_key)
    print("result" + encrypted)
elif(choice == "D"):    
    encryption_key = ''.join(random.sample(alphabet, len(alphabet)))
    print("your key is:" + encryption_key)
    string = input("enter string:")
    while(alphnum > -1 ):
            encrypted = string.replace(alphabet[alphnum], encryption_key[alphnum] )
            print("replaced" + encryption_key[alphnum] + "with" + alphabet[alphnum] + encrypted)
            alphnum = alphnum - 1
            time.sleep(0.5)
    print("your key is" + encryption_key)
    print("your string is" + string)
    
