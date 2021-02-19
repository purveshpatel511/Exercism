# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:

    WORD = None
    GUESS_WORD = ""
    OLD_GUESS_WORD = None
    guesses = list()
    remaining_guesses = 9

    def __init__(self, word):
        self.status = STATUS_ONGOING
        self.WORD = word
        self.OLD_GUESS_WORD = "_" * len(word)
        self.GUESS_WORD = "_" * len(word)
        self.remaining_guesses = 9
        self.guesses = []

    def guess(self, char):
        if self.remaining_guesses < 0 or self.GUESS_WORD == self.WORD:
            raise ValueError("No Guess")

        if char in self.WORD:
            if char in self.guesses:
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE
            else:
                self.guesses.append(char)
            self.GUESS_WORD = ""
            for (c, d) in zip(self.WORD, self.OLD_GUESS_WORD):
                if c == char and d == "_":
                    self.GUESS_WORD += char
                elif d != "_":
                    self.GUESS_WORD += d
                else:
                    self.GUESS_WORD += "_"
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
        self.OLD_GUESS_WORD = self.GUESS_WORD

        if self.GUESS_WORD == self.WORD:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        else:
            self.status = STATUS_ONGOING

        pass

    def get_masked_word(self):
        return self.GUESS_WORD
        pass

    def get_status(self):
        return self.status
        pass


game = Hangman("foobar")

game.guess("b")
print(game.get_status())
print(game.remaining_guesses)