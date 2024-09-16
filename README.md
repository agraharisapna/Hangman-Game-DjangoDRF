#Hangman Game API


** Overview **

This API allows you to play a Hangman game. You can start a new game, check the state of the game, and make guesses. The API is built using Django and Django REST Framework.

Endpoints

    1. Start a New Game
    Endpoint: /game/new
    Method: POST

    Description
        - Starts a new game. A random word is chosen from the list of words, and the player is allowed a number of incorrect guesses   equal to half the length of the chosen word.

    Request Body
        {}
    Response

        {
        "detail": "<game_id>"
        }

    2. Get Game State
    Endpoint: /game/<id>
    Method: GET

    Description
        - Retrieves the current state of the game specified by the game ID.

    Response
        Returns the state of the game including:

        - game_status: The current status of the game (InProgress, Lost, or Won).
        - word: The current state of the word with guessed letters and underscores for unguessed letters.
        - incorrect_guesses: The number of incorrect guesses made.
        - max_incorrect_guess: The maximum number of incorrect guesses allowed.

        {
        "id": "<game_id>",
        "game_status": "InProgress",
        "word": "P__",
        "guessed_letters": "P",
        "incorrect_guesses": 1,
        "max_incorrect_guess": 2
        }

    3. Make a Guess
    Endpoint: /game/<id>/guess
    Method: POST

    Description
        - Submits a single character guess for the game specified by the game ID. Updates the game state based on the guess.

    Request Body

        {
        "guess": "P"
        }
        
    Response
        - Returns the updated game state and indicates if the guess was correct or not.

        {
        "id": "<game_id>",
        "game_status": "InProgress",
        "word": "P__",
        "guessed_letters": "P",
        "incorrect_guesses": 1,
        "max_incorrect_guess": 2
        }

** Models **

    - game_status (CharField): The current status of the game (InProgress, Lost, or Won).
    - word (CharField): The word to be guessed.
    - guessed_letters (TextField): The letters that have been guessed so far.
    - incorrect_guesses (IntegerField): The number of incorrect guesses made.
    - max_incorrect_guess (IntegerField): The maximum number of incorrect guesses allowed.
    - created (DateTimeField): The time when the game was created.

Methods

    - curr_state(): Returns the current state of the word with guessed letters and underscores for unguessed letters.
    - is_lost(): Checks if the game is lost based on the number of incorrect guesses.
    - is_won(): Checks if the game is won based on guessed letters.

** Setup ** 

    Clone the repository.
    Install dependencies: pip install -r requirements.txt.
    Apply migrations: python manage.py migrate.
    Run the server: python manage.py runserver.
