from stats import get_num_of_words
from stats import get_num_of_char
from stats import sort_characters
import sys

def get_book_text(book_path):
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents


def main():
   if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   else: 
       text_from_book = get_book_text(sys.argv[1])
   # file_input = "books/frankenstein.txt"
   

   print("============ BOOKBOT ============ ")
   print("Analyzing book found at", sys.argv[1])

   total_words = get_num_of_words(text_from_book)
   print("----------- Word Count ----------")
   print("Found", len(total_words), "total words")

   total_characters = get_num_of_char(total_words)
   print("--------- Character Count -------")
   sort_characters(total_characters)
   print("============= END ===============")

main()