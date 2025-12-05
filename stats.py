def get_book_text(path_to_file):
    with open(path_to_file) as file:
        contents = file.read()
    return contents

def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    output_dict = {}
    for character in text:
        character = character.lower()
        if character not in output_dict:
            output_dict[character] = 1
        else:
            output_dict[character] += 1
    return output_dict

def get_sorted_char_dict(character_dict):
    char_num_dicts = []
    for character in character_dict:
        num_of_occurences = character_dict[character]
        char_num_dicts.append({"char": character, "num": num_of_occurences})
    char_num_dicts.sort(reverse=True, key=lambda item: item["num"])
    return char_num_dicts