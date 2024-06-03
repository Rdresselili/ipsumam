class Move:
    def __init__(self, name, power, accuracy):
        self.name = name
        self.power = power
        self.accuracy = accuracy

class Moves:
    def __init__(self):
        self.moves = {
            "attack": Move("Attack", 10, 1.0),
            "defend": Move("Defend", 0, 1.0),
            "heal": Move("Heal", -10, 0.5)
        }

    def get_move(self, move_name):
        return self.moves.get(move_name)

# Usage
moves = Moves()
attack_move = moves.get_move("attack")
print(f"{attack_move.name} - Power: {attack_move.power}, Accuracy: {attack_move.accuracy}")
