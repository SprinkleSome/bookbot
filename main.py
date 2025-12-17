from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        text_in_file = f.read()
        return get_num_words(text_in_file)

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"Found {text} total words")

main()