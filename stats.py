def get_num_words(text):
    if type(text) != str:
        raise ValueError("the text argument must be of type str")
    return len(text.split())
