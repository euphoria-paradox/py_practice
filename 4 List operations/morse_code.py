# morse code converter

morse_codes = [('a','.-'), ('b','-...'),('c','-.-.'), ('d','-..'), ('e','.'),
               ('f','..-.'), ('g','--.'),('h','....'),('i','..'),('j','.---'),
               ('k','-.-'),('l','.-..'),('m','--'),('n','-.'),('o','---'),
               ('p','.--.'),('q','--.-'),('r','.-.'),('s','...'),('t','-'),
               ('u','..-'),('v','...-'),('w','.--'),('x','-..-'),('y','-.--'),
               ('z','--..')]

choice = True


    
password = ''
    
while choice:
    which = input('Enter (e) to encrypt / (d) to decrypt: ')

    while which != 'e' and which != 'd':
        which = input('\nInvalid - Enter (e) to encrypt and (d) to decrypt: ')
    
   
    if which == 'e':
        word = input('Enter the word/ sentence to decrypt:')   
        for ch in word:
            for w in morse_codes:
                if ('a' <= ch and ch <= 'z') and ch in w[0]:
                    password = password + ' ' + w[1]

    
        print(word , ': ' ,password)


    else:
        from_index = 1
        to_index = 0
        word = input('Enter the code(separate each code by a space):')
        words = list(word.split(' '))
        for ch in words:
            for code in morse_codes:
                if ch == code[1]:
                    password = password + code[0]
                    letter = True
                
        print(password)
    
    try_again = input('Try again(y or n)')
    if try_again == 'n':
        choice = False