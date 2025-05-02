def count_words(file_contents):
     word_count = 0
     words = file_contents.split()
     for word in words:
          word_count += 1
     return word_count