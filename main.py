from stats import count_words
def get_book_text(path_to_file):
     with open(path_to_file) as f: 
          file_contents = f.read()
          return file_contents

path_to_file = 'books/frankenstein.txt'

def main():
     count_words(get_book_text(path_to_file))
     print(f"{count_words(get_book_text(path_to_file))} words found in the document")
     
main()