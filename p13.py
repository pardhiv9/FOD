import string
from collections import Counter

file_path = "C:/path/to/your/directory/sample_text.txt"


with open(file_path, "r") as file:
    text = file.read()

text = text.lower()
translator = str.maketrans("", "", string.punctuation)
text = text.translate(translator)


words = text.split()


word_counts = Counter(words)


print("Word Frequency Distribution:")
for word, frequency in word_counts.items():
    print(f"{word}: {frequency}")
