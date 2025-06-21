import sys 
def get_num_words(txt_content):
  # print(txt_content)
  word_list = txt_content.split()
  # print(f"{len(word_list)} words found in the document")
  return word_list

def get_char_count(word_list):
  res = {}
  for word in word_list:
    word = word.lower()
    for character in word:
      if character in res:
        res[character] +=1
      else:
        res[character] = 1
  return res



def print_report(wc, res):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {len(wc)} total words")
  print("--------- Character Count -------")
  sorted_res = dict(sorted(res.items(), key = lambda item: item[1], reverse = True))
  for key,value in sorted_res.items():
    if not key.isalpha():
      continue
    print(f"{key}: {value}")
  print("============= END ===============")
