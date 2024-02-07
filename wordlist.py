#!/usr/bin/python3

user_guess = str(input("Guess :"))

with open(f"{user_guess}.txt", "a") as f:
    f.writelines(f"{user_guess}\n")
    for i in range(1000000):
        f.writelines(f"{user_guess}{i}\n")


