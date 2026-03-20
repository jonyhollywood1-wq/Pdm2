# Pocket DM Game Engine
# Basic structure for a Pocket Dungeon Master game engine

class GameEngine:
    def __init__(self):
        self.players = []
        self.current_scene = None

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        print("Game started!")

# Example usage
if __name__ == "__main__":
    engine = GameEngine()
    engine.start_game()