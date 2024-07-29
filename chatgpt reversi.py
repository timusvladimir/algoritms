class Reversi:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 1
        self.board[3][4] = self.board[4][3] = -1
        self.current_player = 1

    def print_board(self):
        for row in self.board:
            print(' '.join(str(x) if x != 0 else '.' for x in row))
        print()

    def is_valid_move(self, x, y, player):
        if self.board[x][y] != 0:
            return False
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == -player:
                while 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == -player:
                    nx += dx
                    ny += dy
                if 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == player:
                    return True
        return False

    def make_move(self, x, y, player):
        self.board[x][y] = player
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            flip_list = []
            while 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == -player:
                flip_list.append((nx, ny))
                nx += dx
                ny += dy
            if 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == player:
                for fx, fy in flip_list:
                    self.board[fx][fy] = player

    def has_valid_moves(self, player):
        for x in range(8):
            for y in range(8):
                if self.is_valid_move(x, y, player):
                    return True
        return False

    def play(self):
        while True:
            self.print_board()
            if not self.has_valid_moves(self.current_player):
                print(f'Player {self.current_player} has no valid moves. Skipping turn.')
                self.current_player = -self.current_player
                if not self.has_valid_moves(-self.current_player):
                    print('Game over!')
                    break
                continue

            x, y = map(int, input(f'Player {self.current_player}, enter your move (row and column): ').split())
            if self.is_valid_move(x, y, self.current_player):
                self.make_move(x, y, self.current_player)
                self.current_player = -self.current_player
            else:
                print('Invalid move. Try again.')

if __name__ == '__main__':
    game = Reversi()
    game.play()



if __name__ == "__main__":
    game = Reversi()
    game.play()
