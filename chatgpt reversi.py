class Reversi:
    def __init__(self):
        self.board = [[' '] * 8 for _ in range(8)]
        self.board[3][3] = 'W'
        self.board[4][4] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.current_player = 'B'

    def display_board(self):
        print("   0  1  2  3  4  5  6  7")
        print("------------------------")
        for i in range(8):
            print(f"{i}| {' | '.join(self.board[i])} |")
            print("------------------------")

    def is_valid_move(self, row, col):
        if self.board[row][col] != ' ':
            return False

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        valid = False

        for d in directions:
            r, c = row + d[0], col + d[1]
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != ' ' and self.board[r][c] != self.current_player:
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == ' ':
                        break
                    elif self.board[r][c] == self.current_player:
                        valid = True
                        break
                    r += d[0]
                    c += d[1]
                if valid:
                    break

        return valid

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False

        self.board[row][col] = self.current_player

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for d in directions:
            r, c = row + d[0], col + d[1]
            to_flip = []

            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == ' ':
                    break
                elif self.board[r][c] == self.current_player:
                    for flip_r, flip_c in to_flip:
                        self.board[flip_r][flip_c] = self.current_player
                    break
                else:
                    to_flip.append((r, c))
                r += d[0]
                c += d[1]

        return True

    def is_game_over(self):
        # Implement logic to check if the game is over
        pass

    def play(self):
        while not self.is_game_over():
            self.display_board()
            print(f"Current Player: {self.current_player}")
            move = input("Enter your move (row col): ").strip().split()
            row = int(move[0])
            col = int(move[1])

            if self.make_move(row, col):
                self.current_player = 'W' if self.current_player == 'B' else 'B'
            else:
                print("Invalid move! Try again.")

        self.display_board()
        print("Game Over!")


if __name__ == "__main__":
    game = Reversi()
    game.play()
