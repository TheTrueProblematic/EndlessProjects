
# Hey there, fellow Pythonista! Ready to play Gomoku (Five in a Row) on your CLI? Well, you're in luck! Let's dive in!

class GomokuGame:
    # Creating our constructor for the game.
    def __init__(self):
        # 15x15 board filled with '-', empty cells:
        self.board = [['-' for _ in range(15)] for _ in range(15)]
        # Starting the game off with player 1:
        self.current_player = "1"
    
    # Function to print the game board.
    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()  # Blank line for aesthetics!

    # Function to get the player's move.
    def get_move(self):
        print(f"Player {self.current_player}'s turn!")
        while True:
            move = input("Enter your move (format 'row column'): ")
            try:
                row, col = map(int, move.split())
                if row<1 or row>15 or col<1 or col>15 or self.board[row-1][col-1] != '-':
                   print("Invalid move! Please enter again.")
                else:
                    return row - 1, col - 1
            except ValueError:
                print("Invalid input! Please enter again.")
                
    # Function to make a move on the board.
    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        # Switching to the other player.
        self.current_player = "2" if self.current_player == "1" else "1"
    
    # Function to check if a player has won.
    def check_winner(self, row, col):
        # Converting cell value to player number.
        player = self.board[row][col]
        
        # Checking all 8 directions from the cell.
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        for dx, dy in directions:
            cnt = 1
            # Forward in current direction.
            x, y = row, col
            while True:
                x, y = x + dx, y + dy
                if x<0 or y<0 or x>=15 or y>=15 or self.board[x][y] != player:
                    break
                # Incrementing counter.
                cnt += 1
            # Backward in current direction.
            x, y = row, col
            while True:
                x, y = x - dx, y - dy
                if x<0 or y<0 or x>=15 or y>=15 or self.board[x][y] != player:
                    break
                # Incrementing counter.
                cnt += 1
            
            # Player wins if counter is 5.
            if cnt >= 5:
                return player
        return None
    
    # Function to play the game.
    def play(self):
        while True:
            self.print_board()
            row, col = self.get_move()
            self.make_move(row, col)
            winner = self.check_winner(row, col)
            if winner:
                print(f"\nCongratulations, Player {winner}! You've won!\n")
                self.print_board()
                break


# Let the games begin!
if __name__ == "__main__":
    game = GomokuGame()
    game.play()
