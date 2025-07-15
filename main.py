from stats import count_words, count_characters


def get_book_text(file_path) -> str:
    with open(file_path) as file:
        book_contents = file.read()
        return book_contents


def main() -> None:
    book_path: str = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    num_words: int = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words.")
    
    print("--------- Character Count -------")
    for character_count in count_characters(get_book_text(book_path)):
        if character_count["character"].isalpha():
            print(f"{character_count['character']}: {character_count['count']}")
    
    print("============= END ===============")


main()
