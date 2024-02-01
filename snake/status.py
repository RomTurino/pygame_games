from enum import Enum

class GameStatus(Enum):
    GAME_ON = "Игра включена"
    GAME_OVER = "Проигрыш"
    GAME_WON = "Победа"

    
game_status = GameStatus.GAME_ON