"""
railfence Cipher encryption and decryption algorithm using Python
Information Security (ICT-3310)

"""
#----------- Decrypt Function -----------------------------
def encrypt(plaintext,key):
    ciphertext = ""
    matrix = [["" for x in range(len(plaintext))] for y in range(key)]
    increment = 1
    row = 0
    col = 0
    for c in plaintext:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[ row ][ col ] = c
        row += increment
        col += 1
    for list in matrix:
        ciphertext += "".join(list)
    return ciphertext.upper()

#----------- Decrypt Function -----------------------------
def decrypt(ciphertext,key):
    plaintext = ""
    matrix = [["" for x in range(len(ciphertext))] for y in range(key)]
    index = 0
    increment = 1
    for selectedRow in range(0, len(matrix)):
        row = 0
        for col in range(0, len(matrix[ row ])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] += ciphertext[index]
                index += 1
            row += increment
    matrix = transpose( matrix )
    for list in matrix:
        plaintext += "".join(list)
    return plaintext.lower()

def transpose( m ):
    output_matrix = [ [ 0 for y in range( len(m) ) ] for x in range( len(m[0]) ) ]
    for i in range( len(m) ):
        for j in range (len(m[0])):
            output_matrix[ j ][ i ] = m[ i ][ j ]
    return output_matrix


def check_key(key):  # Function to check if the key is a valid integer
    while True:
        if key.isdigit():
            return int(key)
        else:
            print("Key is not valid")
            key = input("Enter a valid key: ")


def main():  # Main function for Rail Fence Cipher
    print("************Welcome to Rail Fence Cipher Encryption and Decryption Program************")
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

            key = check_key(key)
            ciphertext = encrypt(plaintext, key)

            print("____________________________________________________________________ ")
            print("\nEncrypted Text using the key of (%d) is : %s " % (key, ciphertext,))
            print("Corresponding Plain Text               : %s " % (plaintext))
            print("____________________________________________________________________ \n")

        elif choice == "2":
            ciphertext = input("\nEnter the cipher text        : ")
            key =        input("Enter the key for decryption : ")

            key = check_key(key)
            plaintext = decrypt(ciphertext, key)

            print("____________________________________________________________________ ")
            print("\nDecrypted Text using the key of (%d) is : %s " % (key, plaintext,))
            print("Corresponding Cipher Text               : %s " % (ciphertext))
            print("____________________________________________________________________ \n")

        elif choice == "3":
            print("____________________________________________________________________ \n")
            print("Exiting the program. Goodbye!")
            print("____________________________________________________________________")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


main()
