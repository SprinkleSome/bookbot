def get_book_text(filepath):
    with open(filepath) as f:
        text_in_file = f.read()
        return number_of_words(text_in_file)

def number_of_words(text):
    return len(text.split())

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"Found {text} total words")

main()