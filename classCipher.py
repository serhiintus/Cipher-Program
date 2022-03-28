class Cipher(object):
    def __init__(self, some_text):
        self.some_text = some_text
    def encryption_bacon(self):
        bacon_cipher_fromalpha = {
            'A':'00000', 'B':'00001', 'C':'00010', 'D':'00011', 'E':'00100', 'F':'00101', 'G':'00110',
            'H':'00111', 'I':'01000', 'J':'01001', 'K':'01010', 'L':'01011', 'M':'01100', 'N':'01101',
            'O':'01110', 'P':'01111', 'Q':'10000', 'R':'10001', 'S':'10010', 'T':'10011', 'U':'10100',
            'V':'10101', 'W':'10110', 'X':'10111', 'Y':'11000', 'Z':'11001'}
        false_message = ''
        num_of_char = 0
        for i in self.some_text:
            if i.isalpha():
                false_message += bacon_cipher_fromalpha[i.upper()]
        num_of_char = len(false_message)
        return (false_message, f'the number of characters is {num_of_char}')
    def decryption_bacon(self):
        bacon_cipher_toalpha = {
            '00000':'A', '00001':'B', '00010':'C', '00011':'D', '00100':'E', '00101':'F', '00110':'G',
            '00111':'H', '01000':'I', '01001':'J', '01010':'K', '01011':'L', '01100':'M', '01101':'N',
            '01110':'O', '01111':'P', '10000':'Q', '10001':'R', '10010':'S', '10011':'T', '10100':'U',
            '10101':'V', '10110':'W', '10111':'X', '11000':'Y', '11001':'Z'}
        binary_group = ''
        original_messsage = ''
        for i in self.some_text:
            if i.isalpha():
                if i.islower():
                    binary_group += '0'
                else:
                    binary_group += '1'
            if len(binary_group) == 5:
                if binary_group in bacon_cipher_toalpha:
                    original_messsage += bacon_cipher_toalpha[binary_group]
                binary_group = ''
        return original_messsage
    def encryption_caesar(self, shift):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ciphertext = ''
        new_letter = ''
        letter_position = None
        for letter in self.some_text:
            letter_position = alphabet.find(letter.lower())
            if letter_position != -1:
                new_letter = alphabet[(letter_position + shift) % len(alphabet)]
            else:
                new_letter = letter
            ciphertext += new_letter
        return ciphertext

    def decryption_caesar(self, shift):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        original_messsage = ''
        new_letter = ''
        letter_position = None
        for letter in self.some_text:
            letter_position = alphabet.find(letter.lower())
            if letter_position != -1:
                new_letter = alphabet[(letter_position - shift) % len(alphabet)]
            else:
                new_letter = letter
            original_messsage += new_letter
        return original_messsage
