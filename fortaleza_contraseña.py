# EJERCICIO 2 VINTAGE

def pass_fort(word):
    numbers = list('1234567890')
    letters = list('abcdefghijklmnñopqrstuvwxyz')
    special_chars = list('!"·$%&//()=€*_:;-.,<>')

    word_str = word     

    # Primer caso contraseña todo numeros y menor de 8 caracteres

    for i in word_str:               
        if i in numbers:
            continue
        elif i in letters:            
            break              
    if len(word_str) < 8:
        checker = '\nMuy Debil'

    # Segundo caso contraseña solo letras y menor de 8 caracteres

    for i in word_str:
        if not i in numbers and len(word_str) < 8:
            checker = '\nDebil'        

    # Tercer caso contraseña con numeros y letras y de al menos 8 caracteres
    for i in word_str:
        if i in numbers or i in letters and len(word_str) == 8:
            checker = '\nFuerte'

    # Cuarto caso contraseña con numeros, letras y caracteres especiales con al menos 8 caracteres

    for i in word_str:
        if i in numbers or i in letters or i in special_chars and len(word_str) >= 8:
            checker = '\nMuy Fuerte'
    
    return checker


print(pass_fort('1234*'))


