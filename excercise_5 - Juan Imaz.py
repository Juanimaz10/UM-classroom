def problem_parrot(speaking, hour):
    if speaking is True and hour < 7 or speaking is True and hour > 20:
        print("True")
    else:
        print("False")


problem_parrot(True,7)