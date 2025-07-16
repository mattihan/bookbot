from stats import get_num_words, get_character_dictionary, get_character_stats
import sys


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

def print_usage():
    print("Usage: python3 main.py <path_to_book>")

def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    BOOK = sys.argv[1]
    try:
        print_book_report(BOOK)

    except ValueError as e:
        print(e)
        sys.exit(3)
    
    except FileNotFoundError as e:
        print(e)
        sys.exit(2)


main()
