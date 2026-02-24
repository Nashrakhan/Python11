# Vowel & Consonants!

n = str(input('Enter a character (a-z): '))

match n:
    case 'a' | 'e' | 'i' | 'o' | 'u' | 'A'| 'E' | 'I' | 'O' | 'U' :
        print('Vowel')

    case _:
        print('Consonant')
