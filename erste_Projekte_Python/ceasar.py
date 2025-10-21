#implementation of ceasar cipher
def encrypt(klar_text:str, key:int)->str:
    return "it is encrypted" + klar_text + "and key" + str(key)

def decrypt(encrypted:str , key:int)->str:
    return "it is decrypted"

def main():
    result = ""
    print("This is ceasar cipher")
    userChoice = input("if you want to encrypt, press e,for decrypt, press d.")

    print(userChoice)
    if (userChoice == 'e'):
        result = encrypt(jojo,5)
        print
    elif (userChoice == 'd'):
        result = decrypt(something,4)
        print(result)
    else:
        print("invalid input,please press e or d.")


if __name__ == "__main__":
    main()

