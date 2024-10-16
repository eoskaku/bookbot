def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) # Type = str
    num_of_words = get_num_words(text)
    chars_dict = get_num_char(text)
    print_report(book_path, num_of_words, chars_dict)

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

def print_report(book, word_count, char_count):
    header = f"--- Begin report of {book} ---\n"
    word_count_text = f"{word_count} words found in the document\n\n"
    alpha_list = filter_dicts_with_alphas(char_count)
    print(header, word_count_text, alpha_list)

def filter_dicts_with_alphas(lst):
    character_list = []
    characters_only_list = []
    for k, v in lst.items():
        character_list.append({k: v})
    for dictionary in character_list:
        all_keys_alpha = True
        for key in dictionary.keys():
            if isinstance(key, str) and not key.isalpha():
                all_keys_alpha = False
            if all_keys_alpha:
                characters_only_list.append(dictionary)
    return characters_only_list


main()