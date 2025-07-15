def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def main():
    print(get_book_text("books/frankenstein.txt"))


main()
