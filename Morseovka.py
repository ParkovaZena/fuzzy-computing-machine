morseov = { 'A':'.-', 
            'B':'-...',
            'C':'-.-.', 
            'D':'-..', 
            'E':'.',
            'F':'..-.',
            'G':'--.', 
            'H':'....',
            'I':'..', 
            'J':'.---', 
            'K':'-.-',
            'L':'.-..', 
            'M':'--', 
            'N':'-.',
            'O':'---', 
            'P':'.--.', 
            'Q':'--.-',
            'R':'.-.', 
            'S':'...', 
            'T':'-',
            'U':'..-', 
            'V':'...-', 
            'W':'.--',
            'X':'-..-', 
            'Y':'-.--', 
            'Z':'--..',
            ' ':' '
}

print("Napis: ")

vstup = input().upper()



for pis in vstup:
    if(pis in morseov.keys()):
        print(morseov[pis],end="")
    else:
        print(" Nepis cisla nejsou tam!!!!!!!!!!!!!!!!!!! ")