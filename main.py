def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   count = get_word_count(text)
   chars = get_char_count(text)
   #print(text)
   print(count)
   print(chars)
 #  sorted_chars = list_chars.sort(reverse=True, key=sort_on)
 #  print(sorted_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(string):
    count = 0
    words = string.split()
    for w in words:
        count += 1
    return count

def get_char_count(text):
    chars = text.lower()
    char_dict = {}
    for c in chars:
        if c.isalpha() == True:
            if c in char_dict:
                char_dict[c] += 1
            else:
              #  check = c
              #  if check.isalpha():
                char_dict[c] = 1
    return char_dict

def sort_on(dict):
    return dict[1]

main()