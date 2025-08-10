def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict:
    chars = {}
    for char in text:
        char = char.lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars


def char_sorted(d: dict) -> list[dict]:
    char_dict_list = []
    for k, v in d.items():
        temp_dict = {}
        temp_dict["char"] = k
        temp_dict["num"] = v
        char_dict_list.append(temp_dict)

    return sorted(char_dict_list, key= lambda x: x['num'], reverse=True)

        