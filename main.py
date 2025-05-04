from stats import count_words
from stats import count_characters
from stats import sort_dictionary
import sys

def get_book_text(path_to_file):
     with open(path_to_file) as f: 
          file_contents = f.read()
          return file_contents

def main():
     if len(sys.argv) < 2:
          print("Usage: python3 main.py <path_to_book>") 
          sys.exit(1)

     file_contents = get_book_text(sys.argv[1])
     word_count = count_words(file_contents)
     character_count = count_characters(file_contents)
     list_of_dictionaries = sort_dictionary(character_count)
     print(f"{word_count} words found in the document")
     print(f"{character_count}")
     print(f"{list_of_dictionaries}")
     print("============ BOOKBOT ============")
     print("Analyzing book found at books/frankenstein.txt...")
     print("----------- Word Count ----------")
     print(f"Found {word_count} total words")
     print("--------- Character Count -------")
     for dict in list_of_dictionaries:
          if dict.get("character").isalpha() == True:
               print(f"{dict.get("character")}: {dict.get("count")}")
     print("============= END ===============")

main()