from stats import get_num_words, get_char_list, sorted_list
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        text_in_file = f.read()
        return text_in_file



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])

    words = get_num_words(text)
    char = get_char_list(text)
    the_list = sorted_list(char)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in the_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()