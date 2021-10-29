#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Oct 2021
# This program formats a string into a frame


def frame_builder(user_sentence):
    # this function formats a sentence to be in a frame
    user_list = user_sentence.split(" ")  # split string into a list

    padded_user_list = []

    largest_word_length = 0
    hr = ""

    for word in user_list:
        if largest_word_length == 0:
            largest_word_length = len(word)
        if len(word) > largest_word_length:
            largest_word_length = len(word)
    for i in range(largest_word_length + 4):
        hr += "*"
    padded_user_list.append(hr)
    for word in user_list:
        while len(word) < largest_word_length:
            word += " "
        padded_word = "* {} *".format(word)
        padded_user_list.append(padded_word)
    padded_user_list.append(hr)

    return padded_user_list


def main():
    # this function gets input
    user_sentence = input("Enter your sentence: ")
    try:
        frame = frame_builder(user_sentence)
        for word in frame:
            print(word)
    except Exception:
        print("Invalid Input")
    print("\nDone")


if __name__ == "__main__":
    main()
