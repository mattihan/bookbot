def get_num_words(text):
    if type(text) != str:
        raise ValueError("the text argument must be of type str")
    return len(text.split())


def get_character_dictionary(text):
    if type(text) != str:
        raise ValueError("the text argument must be of type str")
    character_dictionary = {}
    for character in text:
        character = character.lower()
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary


def get_alphanumeric_keys(dictionary):
    return list(filter(lambda c: c.isalpha(), sorted(dictionary.keys())))


def get_character_stats(book):
    dictionaries = []
    dictionary = get_character_dictionary(book)
    for key in get_alphanumeric_keys(dictionary):
        dictionaries.append({"char": key, "num": dictionary[key]})
    return dictionaries
