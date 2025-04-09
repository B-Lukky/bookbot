def count_words(book_content):
    word_count = 0
    words_str = book_content.split()
    for word in words_str:
        word_count += 1
    return word_count


def count_chars(book_str):
    char_lib = {}
    book_lowercase = book_str.lower()
    for char in book_lowercase:
        if char.isalpha():
            if char in char_lib:
                char_lib[char] += 1
            else:
                char_lib[char] = 1

    sorted_list = []
    for char, count in char_lib.items():
        sorted_list.append({"name": char, "num": count})

    sorted_list.sort(reverse=True, key=lambda x: x["num"])

    return sorted_list
