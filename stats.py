def get_num_of_words(book_words):
    total_words = book_words.split()
    return total_words

def get_num_of_char(words):
    characters = {}
    for word in words:
        word_low = word.lower()
        for char in word_low:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    # print(characters)
    return characters


def sort_characters(char_dict):
    sorted_list = []
    for key in char_dict:
        sorted_dict = {}
        sorted_dict["char"] = key
        sorted_dict["num"] = char_dict[key]
        sorted_list.append(sorted_dict)
    sorted_list.sort(reverse=True, key=sort_on)

    for char in sorted_list:
        print(f"{char["char"]}: {char["num"]}")
    
def sort_on(items):
    return items["num"]