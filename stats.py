def count_words(text: str) -> int:
    word_count = text.split()
    return len(word_count)