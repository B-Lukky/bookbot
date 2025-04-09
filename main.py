from stats import count_words, count_chars
import sys


def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()

    return book_content


def get_book_filepath():
    # file_path = ""
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        file_path = sys.argv[1]
        return file_path


def main():
    book_path = get_book_filepath()
    frankenstein = get_book_text(book_path)

    total_words = count_words(frankenstein)
    unique_words_sorted = count_chars(frankenstein)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char_dict in unique_words_sorted:
        char = char_dict["name"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    print("============= END ===============")


main()
