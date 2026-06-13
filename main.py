import time
import art
from art import *
import colorama
from colorama import init, Fore, Back, Style
import random


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphnum = int(-1)
Art = text2art("VIENCRYPT", chr_ignore=True)
print(Fore.MAGENTA + Art)

print(
    """what do you want to do? :)
     E = Encrypt
     D = Decrypt
     I = Project Info"""
)

choice = input("choose: ")
if(choice == "D"):
    encryption_key = input("enter key: ")
    string = input("enter string: ")
    decrypted = " "
    for char in string:
        if char in alphabet:
            decrypted += alphabet[encryption_key.index(char)]
        else:
            decrypted += char

    print("string " + string + " decrypted with key  " + encryption_key)
    print("result " + decrypted)
elif(choice == "E"):    
    encryption_key = ''.join(random.sample(alphabet, len(alphabet)))
    print("your key is:" + encryption_key)
    string = input("enter string: ")
    encrypted = ""
    for char in string:
        if char in alphabet:
            encrypted += encryption_key[alphabet.index(char)]
        else:
            encrypted += char
    print("your key is " + encryption_key)
    print("your string is " + encrypted)
elif(choice == "I"):
    print(
        """made by violetdoesntexist
        mit licensed full open source
        violetdoesntexist on github discord insta and more+
        hope you like this little dumb program of mine! :3 """
    )