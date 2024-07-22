name = input("Digite seu nome: ")    
name = name.replace(" ", "").lower()
#Inverte o nome!
nameInvert = name[::-1]

if(name == nameInvert):
    print(f'O nome é um Palíndromo! O Nome ({name.capitalize()}) e o Nome Invertido ({nameInvert.capitalize()}) são iguais!')