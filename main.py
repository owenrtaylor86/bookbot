def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   count = get_word_count(text)
   chars = get_char_count(text)
   
   print(f"--- Begin report of {book_path} ---")
   print(f"{count} words found in the document")
   print("")
   chars.sort(reverse=True, key=sort_on)
   display(chars)
   print("--- End report ---")

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
    char_dict = []  # This will be our list of dictionaries
    for c in chars:
        if c.isalpha():
            # Check if there's already a dictionary for this character
            found = False
            for d in char_dict:
                if d["letter"] == c:
                    d["count"] += 1
                    found = True
                    break
            # If not found, add a new dictionary for this character
            if not found:
                char_dict.append({"letter": c, "count": 1})
    return char_dict

def sort_on(dict):
    return dict["count"]

def display(dict_list):
    for l in dict_list:
        letter = l["letter"]
        count = l["count"]
        print(f"The '{letter}' character was found {count} times")

main()