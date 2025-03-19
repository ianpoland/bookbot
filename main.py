from stats import count_words
def get_book_text(filepath):
    #print("here")
    with open(filepath) as f:
        file_content = f.read()
        #print(file_content)
    return file_content
def main():
    #print("here")
    book_content=get_book_text("books/frankenstein.txt")
    num_a = count_words(book_content)
    print(f"{num_a} words found in the document")
    #print(book_content)


main()