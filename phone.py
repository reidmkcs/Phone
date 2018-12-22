"""
Reid Kamhi
phone.py
"""

letters = {}
letters['A'] = '21'
letters['B'] = '22'
letters['C'] = '23'
letters['D'] = '31'
letters['E'] = '32'
letters['F'] = '33'
letters['G'] = '41'
letters['H'] = '42'
letters['I'] = '43'
letters['J'] = '51'
letters['K'] = '52'
letters['L'] = '53'
letters['M'] = '61'
letters['N'] = '62'
letters['O'] = '63'
letters['P'] = '71'
letters['Q'] = '72'
letters['R'] = '73'
letters['S'] = '74'
letters['T'] = '81'
letters['U'] = '82'
letters['V'] = '83'
letters['W'] = '91'
letters['X'] = '92'
letters['Y'] = '93'
letters['Z'] = '94'

def encrypt():
    filename = "original.txt"
    began_line = False
    for line in open(filename):
        for ch in line:
            if ch.isalpha():
                if began_line:
                    print('-', end="")
                print(letters[ch.capitalize()], end="")
                began_line = True
            elif ch == ' ':
                print('')
                began_line = False
            elif ch == "\n":
                print('')
                began_line = False
            elif ch == '-':
                print(' ')
                began_line = True
            else:
                print(ch, end="")
                began_line = True


def decrypt():
    # TODO
    pass


def main():
    option = input("Press \"e\" to encrypt, or press \"d\" to decrypt. ")
    if option == "e":
        encrypt()
    elif option == "d":
        decrypt()
    else:
        print("Program terminated.")

main()