from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        yield (pages.Welcome)

        yield (pages.Sociodemo,
               {'gender': random.randint(1, 3), 'race': random.randint(1, 8), 'age': random.randint(18, 88),
                'education': random.randint(1, 6), 'state': random.randint(1, 51), 'income': random.randint(1, 14)})

        yield (pages.Start)

        if self.player.treat == 1:
            yield (pages.Comprehension, {'distribution': 0, 'infop2': 4, 'earnings1': 2, 'earnings2': 3})
        elif self.player.treat == 2:
            yield (pages.Comprehension, {'distribution': 0, 'infop2': 2, 'infop3': 2, 'earnings1': 2, 'earnings2': 3})
        elif self.player.treat == 3:
            yield (pages.Comprehension, {'distribution': 0, 'infop2': 2, 'infop3': 0, 'earnings1': 2, 'earnings2': 3})
        elif self.player.treat == 4:
            yield (pages.Comprehension, {'distribution': 0, 'infop2': 2, 'infop3': 1, 'earnings1': 2, 'earnings2': 3})
        else:
            yield (pages.Comprehension, {'distribution': 0, 'infop2': 2, 'infop3': 1, 'earnings1': 2, 'earnings4a': 2, 'earnings2':3, 'earnings4b': 1})

        if self.player.treat == 1:
            yield (pages.NoReport)

        if self.player.treat >= 2:
            yield (pages.Report, {'report_2': random.randint(1,30)})

        yield (pages.Beliefintro)

        yield (pages.Beliefsa, {'belief1': random.randint(1,30)})

        if self.player.treat >= 3:
            yield (pages.Beliefsendo, {'belief_endo': True})

        if self.player.treat >= 2:
            yield (pages.Beliefsb, {'belief3': random.randint(1,30)})

        yield (pages.Pretest, {'pretest1': 0, 'pretest2': 1, 'pretest3': 101})


# otree test three_p2 --export=test_three_p2
