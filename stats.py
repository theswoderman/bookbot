def count_words(file_contents):
     word_count = 0
     words = file_contents.split()
     for word in words:
          word_count += 1
     return word_count

def count_characters(file_contents):
     character_dictionary = {}
     characters = list(file_contents)
     for character in characters:
          character_lower = character.lower()
          if((character_lower in character_dictionary) == False):
               character_dictionary[character_lower] = 1
          else:
               character_count = character_dictionary[character_lower]
               character_count += 1
               character_dictionary[character_lower] = character_count
     return character_dictionary

def sort_on(dict):
     return dict["count"]

def sort_dictionary(character_dictionary):
     list_of_dictionaries = []
     for character, count in character_dictionary.items():
          new_dict = {"character": f"{character}", "count": int(count)}
          list_of_dictionaries.append(new_dict)
     list_of_dictionaries.sort(reverse=True, key=sort_on)
     return list_of_dictionaries