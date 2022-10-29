from helpers.get_random_lines import get_random_lines
from helpers.get_current_date import get_current_date

words_file = open("files/words.txt")
words_lines = words_file.readlines()

TOTAL_WORDS = int(words_lines[2])

learned_words = []
dates = []
with open("files/your_words.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        try:
            learned_words.append(int(line.split(" ")[1]))
        except:
            if line != "\n":
                dates.append(line.split("\n")[0])

words_to_learn = input("Enter the number of words to learn (press Enter if you want to choose default = 10) ")
if words_to_learn == "":
    words_to_learn = 10
else:
    words_to_learn = int(words_to_learn)

with open("files/your_words.txt", "a") as f:
    words_idx = get_random_lines(TOTAL_WORDS, learned_words, words_to_learn)

    current_date = get_current_date()
    if current_date not in dates:
        f.write("\n")
        f.write(f"{get_current_date()}\n")

    for idx in words_idx:
        string_to_write = f" {idx} {words_lines[idx]}"
        f.write(string_to_write)

print("Words added to files/your_words.txt")
tmp = input()