def main():
    while True:
        option = int(input("Type 1 for encryption, 2 for decryption, or 0 to quit: "))
        if option == 0:
            quit("Goodbye")
        elif option == 1:
            key = int(input("Enter key, 0-25: "))
            message = input("Enter message (spaces are allowed, punctuation is not): ").upper()
            encrypt(key, message)
        elif option == 2:
            key = int(input("Enter key, 0-25: "))
            encrypted_message = input("Enter encrypted message (spaces are allowed, punctuation is not): ").upper()
            decrypt(key, encrypted_message)
        else:
            continue

def encrypt(key, message):
    letters = {'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7', 'I': '8', 'J': '9',
               'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18',
               'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25'}
    alph_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23, 24, 25]

    message_temp = list(message)
    message_temp = [letters.get(e, e) for e in message_temp]

    for i in range(len(message_temp)):
        if message_temp[i] in alph_numbers:
            message_temp[i] = int(message_temp[i])
    for i in range(len(message_temp)):
        if isinstance(message_temp[i], int):
            message_temp[i] = (message_temp[i] + key) % 26
    for i in range(len(message_temp)):
        if message_temp[i] in nums:
            message_temp[i] = str(message_temp[i])

    encryption = ''
    for i in message_temp:
        if i != ' ':
            encryption += list(letters.keys())[list(letters.values()).index(i)]
        else:
            encryption += ' '
    print("Here is your encrypted message: " + encryption)



def decrypt(key, encrypted_message):
    letters = {'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7', 'I': '8', 'J': '9',
               'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18',
               'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25'}
    alph_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23, 24, 25]

    encrypted_message_temp = list(encrypted_message)
    encrypted_message_temp = [letters.get(e, e) for e in encrypted_message_temp]

    for i in range(len(encrypted_message_temp)):
        if encrypted_message_temp[i] in alph_numbers:
            encrypted_message_temp[i] = int(encrypted_message_temp[i])
    for i in range(len(encrypted_message_temp)):
        if isinstance(encrypted_message_temp[i], int):
            encrypted_message_temp[i] = (encrypted_message_temp[i] - key) % 26
    for i in range(len(encrypted_message_temp)):
        if encrypted_message_temp[i] in nums:
            encrypted_message_temp[i] = str(encrypted_message_temp[i])

    message = ''
    for i in encrypted_message_temp:
        if i != ' ':
            message += list(letters.keys())[list(letters.values()).index(i)]
        else:
            message += ' '
    print("Here is your decrypted message: " + message)



if __name__ == "__main__":
    main()