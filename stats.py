def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    #print(f"{num_words} words found in the document")
    return num_words

def counter(file_contents):
    counted_letters = {}

    for character in file_contents:
        character = character.lower() # Create new list of all characters, but lowercase

        if character in counted_letters:
            counted_letters[character] += 1 #If character is in the dictionary, add 1 to the count of it
        else:
            counted_letters[character] = 1 # otherwise this is the first time seen, set value to 1
    
    return counted_letters

def report(counted_letters): # use dictionary created from counter as input argument

    transformed_list = []
    for char, count in counted_letters.items():
        transformed_list.append({'char': char, 'count': count})

    def get_count(item):
        return item['count']

    transformed_list.sort(key=get_count, reverse=True)
    return transformed_list