def encoder(password):
    encodedPassword = ''
    for i in range(len(password)):
        digit = str((int(password[i]) + 3) % 10)
        encodedPassword += digit
    return encodedPassword

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
