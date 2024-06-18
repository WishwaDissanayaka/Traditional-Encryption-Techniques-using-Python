"""
vigenere Cipher encryption and decryption algorithm using Python
Information Security (ICT-3310)

"""
# Function to encrypt a plain text using Vigenère Cipher
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            # Shift the character based on the corresponding key character
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text.upper()

# Function to decrypt a cipher text using Vigenère Cipher
def vigenere_decrypt(cipher_text, key):
    decrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            # Shift the character based on the corresponding key character
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text.lower()

def check_key(key):  # Checking the key is a value or not
    while True:
        if key.isalpha():
            return key.upper()
            break
        else:
            print("Key is not valid")
            key = input("Enter a valid key: ")

# Home interface for the user
def main():  #main function
    print("************Welcome to Vigenere Cipher Encryption and Decryption Program************")    
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
            plain_text = input("Enter the plain text: ")
            key = input("Enter the key: ")
            key = check_key(key) 

            encrypted_text = vigenere_encrypt(plain_text, key)
            print("Encrypted Text:", encrypted_text)



        elif choice == "2":
            cipher_text = input("Enter the cipher text: ")
            key = input("Enter the key: ")
            key = check_key(key)

            decrypted_text = vigenere_decrypt(cipher_text, key)
            print("Decrypted Text:", decrypted_text)

        elif choice == "3":
            print("____________________________________________________________________ \n")
            print("Exiting the program. Goodbye!")
            print("____________________________________________________________________")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


main()
