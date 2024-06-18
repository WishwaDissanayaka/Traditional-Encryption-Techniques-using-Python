"""
Caesars Cipher encryption and decryption algorithm using Python

"""
def encrypt(text, key): #Encrypting Function
    result = ""
    for letter in text:
        if letter.isalpha():  # Process only alphabetic characters
            ascii_val = ord('A') if letter.isupper() else ord('a')
            encrypted_letter = chr((ord(letter) - ascii_val + key) % 26 + ascii_val)
            result += encrypted_letter
        else:
            result += letter
    if key>0:
        return result.upper()
    else:
        return result.lower()

def decrypt(text, key): #Decrypting Function
    return encrypt(text, -(key))  # Decrypting is done with by converting the key to negative

def check_key(key): #checking the key is a value or not
    while True:
        if key.isdigit():
            return int(key)
        else:
            print("Key is not valid")
            key = input("Enter a valid key: ")

   
def main():  #main function
    print("************Welcome to Caesar's Cipher Encryption and Decryption Program************")    
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
            key =       input("Enter the key for encryption : ")

            key = check_key(key)                                #calling check key function
            ciphertext = encrypt(plaintext, key)

            print("____________________________________________________________________ ")
            print("\nEncrypted Text using the key of (%d) is : %s " % (key, ciphertext,))
            print("Corresponding Plain Text               : %s " % (plaintext))
            print("____________________________________________________________________ \n")

        elif choice == "2":
            ciphertext = input("\nEnter the cipher text        : ")
            key =        input("Enter the key for decryption : ")
            key = check_key(key)                                #calling check key function
            plaintext = decrypt(ciphertext, key)
          
            print("____________________________________________________________________ ")
            print("\nDecrypted Text using the key of (%d) is : %s " % (key, plaintext,))
            print("Corresponding Cipher Text              : %s " % (ciphertext))
            print("____________________________________________________________________ \n")

        elif choice == "3":
            print("____________________________________________________________________ \n")
            print("Exiting the program. Goodbye!")
            print("____________________________________________________________________")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


main()
