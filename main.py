# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import Counter

def read_file_content():
    # [assignment] Add your code here 
    filename = "story.txt"
    with open (filename) as f:
        file = f.read()
        
        return file

print(read_file_content())
print()


def count_word(file_name):
    text = read_file_content()
    #[assignment] Add your code here
    with open(file_name) as f:
        return Counter(f.read().split())

print(count_word("story.txt"))