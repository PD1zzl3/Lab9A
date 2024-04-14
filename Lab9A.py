def encoder(password):
    encodedPassword = ''
    for i in range(len(password)):
        digit = str((int(password[i]) + 3) % 10)
        encodedPassword += digit
    return encodedPassword

# decryption function
def decoder(encodedPassword):
    result = ''
    for i in range(len(encodedPassword)):
        result += str((int(encodedPassword[i]) - 3) % 10)
    return result

def main():
    print('Menu' +
    '\n -------------')

    print(' 1. Encode' +
          '\n 2. Decode' +
          '\n 3.Quit')

    while True:
        print('Please enter an option: ')
        choice = int(input(''))
        if choice == 1:
            password = input('Please enter your passweord to encode: ')
            encodedPassword = encoder(password)
        if choice == 2:
            decodedPassword = decoder(encodedPassword)
            print('The encoded password is: ' + str(encodedPassword) + ', and the decoded password is ' + str(
                decodedPassword))
        if choice == 3:
            return


if __name__ == '__main__':
    main()