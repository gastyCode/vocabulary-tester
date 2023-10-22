import random
import data

score = 0

words_count = len(data.data)
data_list = list(data.data.items())
random.shuffle(data_list)

for i, d in enumerate(data_list):
    print(f"Score: {score}/{words_count}")
    print(f"{i + 1}. {d[0]} == ", end="")
    response = input("")
    if response == d[1]:
        score += 1
    else:
        print(f"---> {d[1]}")

print(f"Your final score is {score}/{words_count} ---> {score / words_count}%")
if score * 0.9 >= words_count:
    print("You are ready for the test.")
else:
    print("You should train more.")
