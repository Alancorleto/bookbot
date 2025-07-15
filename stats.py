def count_words(text: str) -> int:
    word_count = text.split()
    return len(word_count)


def count_characters(text: str) -> list[dict]:
    character_counts: dict[str, int] = {}
    for word in text.lower().split():
        for character in word:
            if not character_counts.get(character):
                character_counts[character] = 1
            else:
                character_counts[character] += + 1
    sorted_character_counts: list[dict] = sort_characters(character_counts)
    return sorted_character_counts


def sort_on(character: dict) -> int:
    return character["count"]


def sort_characters(character_counts: dict[str, int]) -> list[dict]:
    characters = []
    for character, count in character_counts.items():
        characters.append({"character": character, "count": count})
    characters.sort(key=sort_on, reverse=True)
    return characters
