class Connect4:

    def __init__(self):
        
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = 1
        self.game_finished = False
    def play(self, col):
        if self.game_finished:
            print("Game has finished!")

        row = self.get_free_row(col)
        
        if row == None:
            print ("Column full!!")
        
        self.board[row] [col] = self.current_player
        
        if self.winner(row, col):
            self.game_finished = True
            print(f"Player {self.current_player} wins!!!")

        result = f"Player {self.current_player} has a turn"

        if self.current_player == 1:
            self.current_player = 2
        elif self.current_player == 2:
            self.current_player = 1

        print(result)
        
        print(self.board)
    def get_free_row(self,col):
        for row in range(5,-1,-1):
            if self.board[row] [col] == 0:
                return row
            else:
                continue
        return None
    def winner(self, row, col):
        player = self.board[row][col]
        directions = [(0,1),
                      (1,0),
                      (1,1),
                      (1,-1)]
        for row_change,col_change in directions:
            count = 1
            count += self.count_discs(row, col, row_change, col_change, player)
            count += self.count_discs(row, col, -row_change, -col_change, player)

            if count >= 4:
                return True
        return False
    def count_discs(self, row, col, row_change, col_change, player):
        count = 0

        row += row_change
        col += col_change

        while 0 <= row < 6 and 0<= col <7:
            if self.board[row] [col] != player:
                break
            count+=1
            row += row_change
            col += col_change
        return count

                

    


game1 = Connect4()

for y in range(9):
    for x in range (7):
        game1.play(x)