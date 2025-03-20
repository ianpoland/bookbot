def count_words(book):
    words = book.split()
    num_words = len(words)
    return num_words
def count_chars(book):
    char_dict = dict()
    book_as_list = list(book)
    for character in book_as_list:
        chara = character.lower()
        if chara in char_dict.keys():
            char_dict[chara]+=1
        else:
            char_dict[chara] = 1

    return char_dict

def report(char_dict):
    new_dict = dict()
    for key in char_dict.keys():
        if(key.isalpha()):
            new_dict[key] = char_dict[key]
    sorted_dict = dict(sorted(new_dict.items(), key = lambda item : item[1], reverse = True))
    return(sorted_dict)