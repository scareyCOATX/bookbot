from stats import count_characters, count_words, char_sorted


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    char_dict = (char_sorted(char_count))
    print(report(word_count, char_dict, book_path))


def get_book_text(book_path: str) -> str:
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()


def report(word_count, char_dict, book_path):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for i in char_dict:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["num"]}')
        else:
            pass


if __name__ == "__main__":
    main()