
# using wel function to show msg to user
def welcome():
    print('''Welcome to the Caesar Cipher
    This prgram encrypts and decrypts text with the Caesar Cipher''')




# function takes input from the user
def enter_message():
    while True:
        option= input("Would you like to encrypt (e) or decrypt (d)? :").lower()  # Asking user his opinion
        while option != "e" and option != "d":
            option = input("Invalid mode.. Would you like to encrypt (e) or decrypt (d)? :").lower()# Converting into lower case incase if input is in upper case
        
        
        shift_num = int(input("What is the shift number:")) # taking input of his desired shift
        
        #if option equals e msg is encrypted
        if option == "e": 
            msg = input("What message would you like to encrypt:")
            output = encrypt(msg, shift_num)
        #if option equals to d msg is decrypted
        else:
            msg = input("What message would you like to decrypt:")
            output = decrypt(msg, shift_num)
        
        print("Output: " + output) #Final result
        #Asking whether user wants to continue
        again = input("Would you like to encrypt or decrypt another message? (y/n):").lower()
        while again != "y" and again != "n":    # if again  equals y then it goes in loop
            again = input("Invalid  Would you like to encrypt or decrypt another message (y/n)? ").lower()
        
        if again == "n":# if again equals n the loop is terminated and goodbye message is shown
            print('Thanks for using the program, goodbye!')
            break


#using def encrypt fuction  to convert plaintext to ciphertext which means take input 
def encrypt(plain_text, shift_num):
    cipher_text = ""                     #assigning null
    for char in plain_text:    # Checking each character of entered message
        if char.isalpha(): # method returns True if all the characters are alphabet letters (a-z)
            shift_char = chr((ord(char.upper()) + shift_num - 65) % 26 + 65) #converts every alphabet entered by the user to uppercase and checking reminder and adds its ASCII value  which is passed to ciphertext
            cipher_text += shift_char 
    return cipher_text  #returning final value



def decrypt(cipher_text, shift_num): #using def decrypt to convert plaintext to ciphertext which means take input 
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - shift_num - 65) % 26 + 65)#coverts every alphabet entered by the user to uppercase and subtracts its ASCII vaue which is passsed to plaintext
            plain_text += shift_char
    return plain_text




if __name__ == "__main__":  # Normal conditional block to run code as script
    welcome()       # calling function
    enter_message()  # calling function
