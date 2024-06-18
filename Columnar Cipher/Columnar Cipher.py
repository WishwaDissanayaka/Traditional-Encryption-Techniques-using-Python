"""
colunar Cipher encryption and decryption algorithm using Python

"""

def cipher_encryption(plaintext,key):
    plaintext = plaintext.replace(" ", "").upper()

    key = key.upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    extra_letters = len(plaintext) % len(key)
    dummy_characters = len(key) - extra_letters

    if extra_letters != 0:
        for i in range(dummy_characters):
            plaintext += "X"

    num_of_rows = int(len(plaintext) / len(key))

    # Converting plaintext into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = plaintext[z]
            z += 1

    

    # getting locations 
    num_loc = get_number_location(key, kywrd_num_list)


    # cipher text
    cipher_text = ""
    k = 0
    for i in range(num_of_rows):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        k += 1


    return cipher_text


def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
    return num_loc


def keyword_num_assign(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kywrd_num_list = list(range(len(key)))
    # passing(key NumList)
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init

    return kywrd_num_list


def cipher_decryption(ciphertext,key):
    ciphertext = ciphertext.replace(" ", "").upper()

    key = key.upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    num_of_rows = int(len(ciphertext) / len(key))

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    # Converting ciphertext into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    plain_text = ""
    k = 0
    itr = 0

    for i in range(len(ciphertext)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = ciphertext[itr]
            itr += 1
        if itr == len(ciphertext):
            break
        k += 1
    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])
    return plain_text

def check_key(key):  # Checking the key is a value or not
    while True:
        if key.isalpha():
            return key.upper()
            break
        else:
            print("Key is not valid")
            key = input("Enter a valid key: ")

def main():
    """
    Main function to execute the Columnar Transposition Cipher program.
    """
    print("************Columnar Transposition Cipher************")    
    while True:
        print(" ______________")
        print("|              |")
        print("|***Options:***|")
        print("|  1. Encrypt  |")
        print("|  2. Decrypt  |")
        print("|  3. Exit     |")
        print("|              |")
        print("|______________|")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            plaintext = input("\nEnter the plain text         : ")
            key =       (input("Enter the key for encryption : "))
            key = check_key(key)
            ciphertext = cipher_encryption(plaintext, key)

            print("\nEncrypted Text using the key of ({}) is : {}".format(key, ciphertext))

        elif choice == "2":
            ciphertext = input("\nEnter the cipher text        : ")
            key =        (input("Enter the key for decryption : "))
            key = check_key(key)
            plaintext = cipher_decryption(ciphertext, key)

            print("\nDecrypted Text using the key of ({}) is : {}".format(key, plaintext))

        elif choice == "3":
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

main()
