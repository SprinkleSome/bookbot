def get_num_words(text):
    return len(text.split())

def get_char_list(text):
    char_list = {}
    for char in text:
        lower_case = char.lower()
        if lower_case in char_list:
            char_list[lower_case] += 1
        else:
            char_list[lower_case] = 1
    return char_list

def frequency(the_list):
    return the_list["num"]

def sorted_list(dic):
    new_list = []
    for thing in dic:
        pair = {"char": thing, "num": dic[thing]}
        new_list.append(pair)
        new_list.sort(reverse = True,key = frequency)
    return new_list
        