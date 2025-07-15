from stats import get_num_words


def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def main():
    try:
        print(f"{get_num_words(get_book_text("books/frankenstein.txt"))} words found in the document")
    except Exception as e:
        print(e)


main()
