def get_book_text(filepath):
    with open(filepath) as f:
        text_in_file = f.read()
        return text_in_file

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)

main()