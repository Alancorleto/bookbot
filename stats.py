def count_words(text: str) -> int:
    word_count = text.split()
    return len(word_count)


def count_characters(text: str) -> dict[str, int]:
    character_counts: dict[str, int] = {}
    for word in text.lower().split():
        for character in word:
            if not character_counts.get(character):
                character_counts[character] = 1
            else:
                character_counts[character] += + 1
    return character_counts
