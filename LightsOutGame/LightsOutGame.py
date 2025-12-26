# Here is a simple, fun, and lovely Python code for a CLI version of the "Lights Out" game. Oh my, isn't coding just a blast!

# Hey there, fellow coder! Let's kickstart this amazing day with a cool puzzle game: Lights Out. So, get ready, it's going to be a fantastic journey!

class LightsOutGame:
    # First things first, let's define our board size. Coding is all about customization, you know!
    def __init__(self, size=5):
        self.size = size
        self.board = [[0]*size for _ in range(size)]

    # Toggling is fun, isn't it? Especially when it builds the logic of our game! 
    def toggle(self, x, y):
        # We will toggle a cell and its neighbours (Oh dear, this really keeps my AI gears turning!)
        for dx, dy in [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.board[nx][ny] = 1 - self.board[nx][ny]
    
    # Now comes the interesting part - playing the game! I am really looking forward to this!
    def play(self):
        # The game should be played until all lights go out
        while any(any(row) for row in self.board):
            # Print the board (Oh, I love visualizing stuff!)
            for row in self.board:
                print(''.join('#' if cell else '.' for cell in row))
            print()

            # Get user input and toggle cells
            x, y = map(int, input('Enter the coordinates to toggle (x y): ').split())
            self.toggle(x, y)

if __name__ == "__main__":
    # We are now ready to rumble! Initiate the game and let's have some fun!
    game = LightsOutGame()
    game.play()

# This simple, but wildly entertaining, piece of code creates a splendid 'Lights Out' game, which is played right in the command line. We hope you enjoy it as much as we enjoyed crafting it. Happy coding!