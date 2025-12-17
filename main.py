from stats import get_num_words, get_char_list

def get_book_text(filepath):
    with open(filepath) as f:
        text_in_file = f.read()
        return text_in_file



def main():
    text = get_book_text("./books/frankenstein.txt")
    words = get_num_words(text)
    print(f"Found {words} total words")

main()