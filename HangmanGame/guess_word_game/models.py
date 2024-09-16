from django.db import models
import random
from django.utils import timezone
# Create your models here.


class Game(models.Model):

    WORD_LIST = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]

    IN_PROGRESS = 'InProgress'
    LOST = 'LOST'
    WON = 'WON'
    
    STATUS_OF_GAME = [
        (IN_PROGRESS, 'In Progress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    ]
    game_status = models.CharField(
        max_length=10,
        choices=STATUS_OF_GAME,
        default=IN_PROGRESS,
    )
    word = models.CharField(max_length=100)
    guessed_letters = models.TextField(default='')
    incorrect_guesses  = models.IntegerField(default=0)
    max_incorrect_guess = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)


    def curr_state(self):
        state = ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)
        return state
    
    def is_lost(self):
        return self.incorrect_guesses >= self.max_incorrect_guess
    
    def is_won(self):
        return set(self.word) <= set(self.guessed_letters)
    
    def __str__(self):
        return self.word
    
