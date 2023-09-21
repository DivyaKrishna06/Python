class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)


class Game:
    def __init__(self):
        self.current_room = None
        self.moves = 0

    def create_rooms(self):
        room1 = Room("Living Room", "You are in a cozy living room with a fireplace.")
        room2 = Room("Kitchen", "You are in a bright kitchen with a large window.")
        room3 = Room("Bedroom", "You are in a comfortable bedroom with a big bed.")

        room1.add_exit("east", room2)
        room2.add_exit("west", room1)
        room2.add_exit("south", room3)
        room3.add_exit("north", room2)

        self.current_room = room1

    def start(self):
        print("Welcome to the Text Adventure Game!")
        self.create_rooms()
        self.play()

    def play(self):
        while True:
            print("\n" + self.current_room.name)
            print(self.current_room.description)

            if self.moves > 0:
                print(f"Total moves: {self.moves}")

            user_input = input("Enter a direction (or 'quit' to exit): ").lower()

            if user_input == 'quit':
                print("Thanks for playing!")
                break

            if user_input in self.current_room.exits:
                self.current_room = self.current_room.get_exit(user_input)
                self.moves += 1
            else:
                print("Invalid direction. Try again.")


if __name__ == "__main__":
    game = Game()
    game.start()