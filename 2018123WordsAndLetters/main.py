def count_characters_from_file(fileName, ignoreSpace = True):
    f = open(fileName, 'r')
    characters = dict()
    while True:
        character = f.read(1)
        if not character:
            for i in characters:
                print(f"| {i} | {characters[i]} |")
            print()
            break
        else:
            if character == ' ' and ignoreSpace == True:
                pass
            else:
                if character in characters.keys():
                    characters[character] += 1                       
                else:
                    characters[str(character).lower()] = 1

def count_words_from_file(fileName):
    file = open(fileName, 'r')
    words = dict()
    for line in file:
        for word in line.split():
            if word in words.keys():
                words[word] += 1
            else:
                words[str(word).lower()] = 1
    for i in words:
        print(f"| {i} | {words[i]} |")

if __name__ == "__main__":
    count_characters_from_file('file.txt', False)
    count_words_from_file('file.txt')

    

                                        





















                                                                                                                                                                                                                                                