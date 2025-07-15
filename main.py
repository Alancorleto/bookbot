def get_book_text(file_path) -> str:
    with open(file_path) as file:
        book_contents = file.read()
        return book_contents


def main() -> None:
    print(get_book_text("books/frankenstein.txt"))


main()
