
def get_book_text(path_to_file):
     with open(path_to_file) as f: 
          file_contents = f.read()
          return file_contents

path_to_file = 'books/frankenstein.txt'
def main():
     print(get_book_text(path_to_file))
     
main()