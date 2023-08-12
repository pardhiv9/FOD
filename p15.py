likes_data = [10, 25, 15, 10, 30, 20, 10, 15, 25, 20, 10, 15, 30, 20]

likes_frequency = {}

for likes in likes_data:
    if likes in likes_frequency:
        likes_frequency[likes] += 1
    else:
        likes_frequency[likes] = 1


print("Likes Frequency Distribution:")
for likes, frequency in likes_frequency.items():
    print(f"{likes} likes: {frequency} posts")
