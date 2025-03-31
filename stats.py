def word_count(book_text):
    return len(book_text.split())

def character_count(book_text):
    char_count = {}
    for word in book_text.lower():
        for letter in word:
            try:
                char_count[letter] += 1
            except:
                char_count[letter] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def sort_char_count(char_count):
    sorted_char_count_list = [{"letter": k, "count": char_count[k]} for k in char_count]
    sorted_char_count_list.sort(reverse=True, key=sort_on)
    return sorted_char_count_list

    
    