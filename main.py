from stats import *
import sys
def get_book_text(filepath):
    #print("here")
    with open(filepath) as f:
        file_content = f.read()
        #print(file_content)
    return file_content
def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content=get_book_text(book_path)
    num_a = count_words(book_content)
    char_dict = count_chars(book_content)
    #print(char_dict)
    sorted_repo = report(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_a} total words")
    print("--------- Character Count -------")
    for key in sorted_repo.keys():
        print(f"{key}: {sorted_repo[key]}")
    #print(sorted_repo)
    print("============= END ===============")

main()