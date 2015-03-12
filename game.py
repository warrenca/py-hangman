import re
from sys import exit


class Game(object):
    players = []
    word = None
    redacted_word = None
    mistakes = {}
    points = {}
    winner = False
    current_player = 0
    guess_list = []

    def __init__(self, players, word):
        self.players = players
        self.word = word
        self.redacted_word = re.sub('[a-zA-Z\d]', '*', word)
        self.current_player = 0

    def play(self):
        is_winner = False

        while not self.winner:
            self.show_scores()
            self.display_reducted_word()
            players_name = self.players[self.current_player]
            guess = raw_input("Player '%s' to answer:" % players_name)

            # check for a correct answer
            points = self.get_points(guess)

            self.set_scores(points)

            is_winner = self.check_winner()

            if is_winner:
                self.end(self.current_player)

    def set_scores(self, points):
        players_name = self.players[self.current_player]

        if points > 0:  # if answer matched something, then assign the points to current player
            if players_name in self.points:
                self.points[players_name] += points
            else:
                self.points[players_name] = points
        else:  # add +1 to players mistake
            if players_name in self.mistakes:
                self.mistakes[players_name] += 1
            else:
                self.mistakes[players_name] = 1

            # remove player if mistake has reached the limit
            if self.mistakes[players_name] >= 3:
                self.remove_player()
            else:
                # get the next player
                self.get_next_player()

    def get_next_player(self):
        self.current_player += 1

        if self.current_player >= len(self.players):
            self.current_player = 0

    def remove_player(self):
        print "Player '%s' is eliminated." % self.players[self.current_player]
        self.players.remove(self.players[self.current_player])

    def get_points(self, guess):
        positions = []

        # Check for multiple character guesses
        if (self.check_duplicate_guess(guess.lower())!=True):
            # loop through the characters in self.word
            positions = self.check_for_matches(guess, positions)

        return len(positions)

    def check_for_matches(self, guess, positions):
        i = 0
        for c in self.word:
            # check each character if equal to the guessed character and not in self.guess_list
            if c.lower() == guess.lower():
                positions.append(i)
                self.guess_list.append(guess.lower())

            i += 1

        # if the guessed character matched at least one in the self.word
        if len(positions) > 0:
            redacted_word_array = list(self.redacted_word)

            # replace the self.redacted_word with the correct guess
            i = 0
            for c in self.redacted_word:
                if i in positions:
                    redacted_word_array[i] = guess.upper()
                i += 1

            self.redacted_word = "".join(redacted_word_array)

        return positions

    def check_duplicate_guess(self, guess):
        if guess in self.guess_list:
            print "The character '%s' has already been entered." % guess.lower()
            return True

    def check_winner(self):
        if '*' not in list(self.redacted_word):
            return True

        if len(self.players) == 1:
            return True

        return False

    def display_reducted_word(self):
        print "\n"
        print self.redacted_word
        print "\n"

    def show_scores(self):
        print "Name    | Points | Mistakes |"
        for name in self.players:
            points = 0 if name not in self.points else self.points[name]
            mistakes = 0 if name not in self.mistakes else self.mistakes[name]
            print "%s | %s | %s |" % (name.ljust(7), str(points).ljust(6), str(mistakes).ljust(8))

    def end(self, current_player):
        print "The word is -==%s==-" % self.word.upper()
        print "The winner is \"%s\"!" % self.players[current_player]
        exit()