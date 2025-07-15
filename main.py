from stats import count_words, count_characters


def get_book_text(file_path) -> str:
    with open(file_path) as file:
        book_contents = file.read()
        return book_contents


def main() -> None:
    num_words: int = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    for character, count in count_characters(get_book_text("books/frankenstein.txt")).items():
        print(f"'{character}': {count}")


main()
