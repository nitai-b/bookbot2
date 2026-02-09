def get_book_text():
    path_to_file = "../bookbot2/books/frankenstein.txt"
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_words_in_book():
    return len(get_book_text().split())

def get_character_count():
    text = get_book_text().lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

