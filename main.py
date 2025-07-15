def get_book_text(file_path) -> str:
    with open(file_path) as file:
        book_contents = file.read()
        return book_contents


def count_words(book_path: str) -> int:
    book_text = get_book_text(book_path)
    words = book_text.split()
    return len(words)


def main() -> None:
    num_words: int = count_words("books/frankenstein.txt")
    print(f"{num_words} words found in the document")


main()
