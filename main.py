def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) # Type = str
    num_of_words = get_num_words(text)
    chars_dict = get_num_char(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_count = {}
    lowered_words = text.lower()
    for word in lowered_words:
        if word in char_count:
            char_count[word] += 1
        else:
            char_count[word] = 1
    return char_count


main()