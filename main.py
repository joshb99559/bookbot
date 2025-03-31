from stats import word_count, character_count, sort_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents



def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_source = sys.argv[1]
    print("=========BOOKBOT==========")
    print("Analyzing book found at", )

    words = word_count(get_book_text(book_source))
    print('-------- Word Count --------')
    print("Found", words, "total words")
    #print(character_count(get_book_text(book_source)))

    print('-------- Character Count ------')
    sorted_char_count_list = sort_char_count(character_count(get_book_text(book_source)))
    for item in sorted_char_count_list:
        if (item["letter"].isalpha()):
            print("%s: %d" % (item["letter"], item["count"]))

main()