from stats import *

def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()

    return book_content

def main():
    print(f"{count_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()