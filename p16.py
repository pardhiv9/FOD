import string
customer_reviews = [
    "Great product, highly recommend!",
    "The quality of the product is amazing.",
    "Not satisfied with the product, would not buy again.",
    "Excellent customer service, prompt response.",
    "Product arrived on time, packaging was damaged."
]


word_frequency = {}


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words


for review in customer_reviews:
    words = preprocess_text(review)
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

print("Word Frequency Distribution:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
  
