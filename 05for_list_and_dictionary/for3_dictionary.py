# coding=utf-8

dictionary = {
    "name" : "Janis Joplin",
    "favourite_music" : "One Night Stand"
}

for key , value in dictionary.items():
    print("%s --> %s "  %(key , value))


# Saída
#    favourite_music --> One Night Stand
#    name --> Janis Joplin


'''
    No exemplo acima usamos o método items(),
    ele nos permite ter acesso aos valores, além das
    chaves (que ja temos acesso por padrão)

'''