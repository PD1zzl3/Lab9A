def encoder(password):
    encodedPassword = ''
    for i in range(len(password)):
        digit = str((int(password[i]) + 3) % 10)
        encodedPassword += digit
    return encodedPassword

