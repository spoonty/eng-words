import random


def get_random_lines(selection_range, exceptions = [], num_of_lines = 10):
    random_lines = []

    for i in range(num_of_lines):
        random_int = random.randint(0, selection_range - 1)
        if random_int not in random_lines and random_int not in exceptions:
            random_lines.append(random_int)

    return random_lines