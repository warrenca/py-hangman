from random import randint


class Words(object):
    word_lists = []

    def get_word_lists(self):
        return [word.strip() for word in open('words.txt', 'r')]

    def get_word(self):
        word_lists = self.get_word_lists()
        return word_lists[randint(0, len(word_lists)-1)]