def hangman():
    correct = False
    while not correct:
        try:
            x = 0
            word_guest = "kkw"
            for x in range(2, -1, -1):
                word = input("Enter a word:")
                if word.lower() != word_guest:
                    print("Incorret")
                    print("You have", x, "more guesses left.")
                if word.lower() == word_guest:
                    print("You right,Congratz")
                    break
                if x == 0:
                    print("Thank for playing. The answer is ", word_guest, ".")
            correct = True
        except ValueError:
            print("Invalid")
hangman()

