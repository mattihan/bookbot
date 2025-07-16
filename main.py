from stats import get_num_words, get_character_dictionary, get_character_stats


def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def format_counts_report(counts):
    return '\n'.join(list(map(lambda k: f"{k["char"]}: {k["num"]}", counts)))

def print_book_report(book_path):
    book = get_book_text(book_path)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...""")
    print(f"""----------- Word Count ----------
Found {get_num_words(book)} total words""")
    character_counts = get_character_stats(book)
    print(f"""--------- Character Count -------\n{format_counts_report(character_counts)}""")
    print("============= END ===============")

def main():
    FRANKENSTEIN = "books/frankenstein.txt"
    try:
        print_book_report(FRANKENSTEIN)

    except ValueError as e:
        print(e)


main()
