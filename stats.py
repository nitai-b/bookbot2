import itertools

def get_book_text(book_path):
    # path_to_file = "../bookbot2/books/frankenstein.txt"
    file_contents = ""
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def get_words_in_book(book_path):
    return len(get_book_text(book_path).split())

def get_character_count(book_path):
    text = get_book_text(book_path).lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_alphabetic_characters(book_path):
    alphabetic_list = []
    char_dict = get_character_count(book_path)

    for char, count in char_dict.items():
        if char.isalpha():
            alphabetic_list.append({"char": char, "num": count})

    return sorted(alphabetic_list, key= lambda dict: dict["num"], reverse=True)

def get_top_frequent_characters(k, book_path):
    return get_alphabetic_characters(book_path)[:k]


