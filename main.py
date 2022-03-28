from classCipher import Cipher


while True:
    print('**************************************************')
    print('\tThe Cipher Program v.1.0\n**************************************************')
    print('\n\t\tMain Menu')
    print("1 - to encrypt the message with the Caesar cipher")
    print("2 - to decrypt the message with the Caesar cipher")
    print("3 - to encrypt the message with the Bacon's cipher")
    print("4 - to decrypt the message with the Bacon's cipher\n")


    choice = input('Make your choice: ')
    some_text = Cipher(input('Then enter your message: '))
    if len(some_text.some_text) < 1:
        print('You entered an empty message, try again.')
    else:
        match choice:
            case '1':
                shift = int(input('Enter an alphabetical shift, it must be an integer: '))
                print(f'\n{some_text.encryption_caesar(shift)}\n')
            case '2':
                shift = int(input('Enter an alphabetical shift, it must be an integer: '))
                print(f'\n{some_text.decryption_caesar(shift)}\n')
            case '3':
                print(f'\n{some_text.encryption_bacon()}\n')
                print('To finish encryption you have to prepare a false message')
                print('with the same number of letters as all of the 0s and 1s')
                print('in the string. 0s represent letter in lowercase,')
                print('1s represent letter in uppercase.\n')
            case '4':
                print(f'\n{some_text.decryption_bacon()}\n')
            case _:
                print('\nMake a correct choice\n')
