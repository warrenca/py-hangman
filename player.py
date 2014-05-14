import re


class Player(object):
    players = []
    minimum_players = 2
    maximum_players = 5

    def __init__(self):
        self.add_player()

    def add_player(self):
        print "Please add players (min: %d and max: %d)." % (self.minimum_players, self.maximum_players)
        continue_adding_players = True

        # Add while users wants to add
        # Min self.minimum_players and max self.maximum_players
        while continue_adding_players:
            player_number = len(self.players) + 1
            name = raw_input("Add Player #%d: " % player_number)
            if name:
                self.players.append(name[:7].upper())

            player_count = len(self.players)

            if player_count >= self.maximum_players:
                continue_adding_players = False
            else:
                if player_count >= self.minimum_players:
                    answer_to_continue_adding_players = raw_input("Press 'Y' to add more players? ")

                    required_answer_re = re.compile('[y|yes]', re.IGNORECASE)
                    if required_answer_re.match(answer_to_continue_adding_players):
                        continue_adding_players = True
                    else:
                        continue_adding_players = False


    def get_players(self):
        return self.players