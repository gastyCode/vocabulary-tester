from colorise import cprint
from enum import Enum
from pyfiglet import Figlet
import os
import sys

import data
import random


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Modes(ExtendedEnum):
    TRAIN = "train"
    TRAIN_ALL = "train-all"
    LEARN = "learn"
    LEARN_ALL = "learn-all"


def print_header():
    custom_figlet = Figlet(font="chunky")
    cprint(custom_figlet.renderText("VOCABULARY\nby gastyCode"), fg="red")


def clear_console():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def train(words_list, write_to_file=True):
    if len(words_list) <= 0:
        main()

    score = 0
    words_count = len(words_list)
    random.shuffle(words_list)

    if write_to_file:
        trainer_file = open(data.file_name, "w")

    for i, d in enumerate(words_list):
        cprint(f"Score: {score}/{words_count}", "green")
        print(f"{i + 1}. {d[0]} == ", end="")

        response = input("")
        if response == d[1]:
            score += 1
        else:
            print(f"---> {d[1]}")
            if write_to_file:
                trainer_file.write(f"{d[0]},{d[1]}\n")

    if write_to_file:
        trainer_file.close()

    print(f"Your final score is {score}/{words_count} ---> {(score / words_count) * 100}%")
    if score * 0.9 >= words_count:
        cprint("You are ready for the test.", fg="green")
    else:
        cprint(f"You should train more. Try 'learn' or 'train' command and get better.", fg="red")


def learn(words_list):
    if len(words_list) <= 0:
        main()

    response = ""

    random.shuffle(words_list)
    for i, d in enumerate(words_list):
        while response != d[1]:
            cprint(f"{i + 1}. {d[0]} == {d[1]}", "yellow")
            response = input("Write the word in english: ")

    cprint("You should be ready for the trainer.", fg="green")


def get_file_data():
    words = []
    with open(data.file_name) as data_file:
        for line in data_file.read().splitlines():
            parsed_line = tuple(line.split(","))
            words.append(parsed_line)
    return words


def read_mode():
    modes = Modes.list()
    user_mode = ""
    while user_mode.lower() not in modes:
        clear_console()
        print_header()
        cprint("__________________________________________________________________________________________________________________\n\n", fg="green")
        cprint("'train'      - train only words you don't know (YOU NEED TO USE 'learn-all' COMMAND AT LEAST ONCE TO USE THIS MODE)", fg="yellow")
        cprint("'train-all'  - train all the words you need to know", fg="yellow")
        cprint("'learn'      - learn words that you don't know", fg="yellow")
        cprint("'learn-all'  - learn all the words you need to know", fg="yellow")
        user_mode = input("Select mode: ")
    return Modes(user_mode.lower())


def main():
    mode = read_mode()
    clear_console()

    if mode == Modes.LEARN:
        learn(get_file_data())
    elif mode == Modes.LEARN_ALL:
        learn(list(data.words.items()))
    elif mode == Modes.TRAIN:
        train(get_file_data(), False)
    elif mode == Modes.TRAIN_ALL:
        train(list(data.words.items()))


if __name__ == "__main__":
    main()
