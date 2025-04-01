def count_words(book_content):
    word_count = 0
    words_str = book_content.split()
    for word in words_str:
        word_count += 1
    return word_count