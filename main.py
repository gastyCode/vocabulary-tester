import random
import data

score = 0

words_count = len(data.words)
data_list = list(data.words.items())
random.shuffle(data_list)

trainer_file = open(data.file_name, "w")

for i, d in enumerate(data_list):
    print(f"Score: {score}/{words_count}")
    print(f"{i + 1}. {d[0]} == ", end="")
    response = input("")
    if response == d[1]:
        score += 1
    else:
        print(f"---> {d[1]}")
        trainer_file.write(f"{d[1]} == {d[0]}\n")

trainer_file.close()
print(f"Your final score is {score}/{words_count} ---> {(score / words_count) * 100}%")
if score * 0.9 >= words_count:
    print("You are ready for the test.")
else:
    print(f"You should train more. Look at {data.file_name} where you can train the words you don't know.")
