# coding=utf-8

dictionary = {
    "name" : "Janis Joplin",
    "favourite_music" : "One Night Stand"
}


for key in dictionary: 
    print("%s --> %s " %(key , dictionary[key]))


# Saída
#    favourite_music --> One Night Stand
#    name --> Janis Joplin


''' 
    Quando acessamos dicionários em Python, estamos 
    acessando sua chave e não o valor, no exemplo acima 
    key equivale a "name" e no segundo loop equivale a "favourite_musica"

'''