from cs50 import get_string

puntuacion = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
frase = get_string("Frase : ")
letras = 0.00
frases = 0.00
palabras = 1.0

for n, char in enumerate(frase):
    if (frase[n] != ' ' and frase[n].isalpha()):
        letras += 1
    elif (frase[n] == '.' or frase[n] == '?' or frase[n] == '!') and (n == len(frase)-1 or frase[n+1].isspace() or frase[n+1] in puntuacion):
        frases += 1
    elif (frase[n].isspace() or n == len(frase) - 1):
        palabras += 1

L = (letras*100) / palabras
S = (frases*100) / palabras

index = round(0.0588 * L - 0.296 * S - 15.8)

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
