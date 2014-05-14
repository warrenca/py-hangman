from game import Game
from player import Player
from words import Words


player = Player()
word = Words()

game = Game(player.get_players(), word.get_word())
game.play()