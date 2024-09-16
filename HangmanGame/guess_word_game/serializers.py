from .models import *
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'game_status', 'word', 'guessed_letters', 'incorrect_guesses', 'max_incorrect_guess']
        read_only_fields=['word', 'max_incorrect_guess']
   

    def get_incorrect_guess(self, obj):
        return obj.max_incorrect_guess - obj.incorrect_guesses
    
    def get_curr_status(self, obj):
        return obj.curr_state()
        
    def get_game_status(self, obj):
        if obj.is_lost():
            return Game.LOST
        elif obj.is_won():
            return Game.WON
        return Game.IN_PROGRESS