import sys
from stats import get_alphabetic_characters, get_words_in_book
from stats import get_character_count
from stats import get_top_frequent_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {get_words_in_book(book_path)} total words")
    print("--------- Character Count -------")
    for item in get_alphabetic_characters(book_path):
        print(f"{item['char']}: {item['num']}")
    print("------ Top Character Count ------")
    for item in get_top_frequent_characters(10, book_path):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
