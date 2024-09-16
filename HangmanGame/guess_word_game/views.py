from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer
import random


class NewGameAPI(APIView):
    
    def post(self, request):
            serializer = GameSerializer(data=request.data)
            if serializer.is_valid():
                word = random.choice(Game.WORD_LIST)
                max_incorrect_guess = len(word)//2
                serializer.save(word=word, max_incorrect_guess=max_incorrect_guess)

                return Response({"detail": serializer.data.get('id')}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameStateAPI(APIView):
    def get(self, request, id):
        try:
            game = Game.objects.get(id=id)
        except Game.DoesNotExist:
            return Response({'detail': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = GameSerializer(game)    
        return Response(serializer.data, status=status.HTTP_200_OK)

class GuessGameAPI(APIView):
      def post(self, request, *args, **kwargs):

        game_id = kwargs.get('id')  
        guess_name = request.data.get('guess', '')
        

        if not guess_name: 
            return Response({'detail': 'No guess provided'}, status=status.HTTP_400_BAD_REQUEST)

        
        if len(guess_name)!=1 or not guess_name.isalpha():
              return Response({'detail': 'Invalid guess'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({'detail': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
        if game.game_status != Game.IN_PROGRESS:
               return Response({'detail': 'Game has already ended'}, status=status.HTTP_400_BAD_REQUEST)
        
        if guess_name in game.guessed_letters:
            return Response({'detail': 'Letter already guessed'}, status=status.HTTP_400_BAD_REQUEST)
        
        game.guessed_letters += guess_name

        if guess_name not in game.word:
            game.incorrect_guesses +=1
        
        if game.is_won():
            game.game_status = Game.WON
        elif game.is_lost():
            game.game_status = Game.LOST        
                  
        game.save()
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

