from stats import *
import sys

def get_book_text(path):
  with open(path) as f:
    txt_content = f.read()
  return txt_content


def main():
  print("-------")
  if(len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  txt_content = get_book_text(sys.argv[1])
  word_list = get_num_words(txt_content)
  res = get_char_count(word_list)
  print_report(word_list, res)


main()