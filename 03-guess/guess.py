from random import randint
# add any required imports

# Hey! This get_int() function looks familiar. Copy the implementation of this
# function from get-int.py. If you didn't get that one working right, then just
# leave the default implementation below. Your game should still work. It'll
# just not be as good.


def get_int(prompt, min_val, max_val):
    """Retrieve a number from a user between the specified values."""
    while True:
        user_val = input(prompt)
        try:
            number = int(user_val)
        except ValueError:
            print("NOT A NUMBER")
            continue
        if number < min_val or number > max_val:
            print("OUT OF RANGE")
            continue
        return number


def game(max_guess, num_guesses):
    """Play a super-fun guessing game!!"""
    right_numb = randint(1, max_guess)
    guess_count = 0
    while guess_count < num_guesses:
        guess = get_int(f"Enter a number from 1 to {max_guess}: ", 1, max_guess)
        guess_count += 1
        if guess == right_numb:
            return True
        elif guess < right_numb:
            print("Too Low!")
        elif guess > right_numb:
            print("Too High!")
    print(f"SORRY, IT WAS {right_numb}.")
    return False

###############################################################################
# main function. Look but no need to touch.
###############################################################################


def main():
    """Main entry point for the program."""
    result = game(20, 5)
    if result == True:
        print("Congratulations on your win!")
    elif result == False:
        print("Oh well. You should try again!")
    else:
        print("ERROR! DID YOU FORGET TO RETURN TRUE OR FALSE??")


if __name__ == "__main__":
    main()
