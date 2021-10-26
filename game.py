import time

class Game:
            
    def __init__(self):
        
        self.init_game()
        
    def init_game(self):
        self.current_state = [[".", ".", "."],
                              [".", ".", "."],
                              [".", ".", "."]]
                
        self.player_turn = "X"
    
    def draw_board(self):
        
        for i in  range(0, 3):
            for j in range(0, 3):
                print("{}|".format(self.current_state[i][j]), end = " ")
            print()
        print()
    
    def is_valid(self, p_x, p_y):
        
        if p_x < 0 or p_x > 2 or p_y < 0 or p_y > 2:
            return False
        elif self.current_state[p_x][p_y] != ".":
            return False
        else:
            return True
     
    def is_complete(self):
        
        for i in range(0, 3):
            if (self.current_state[0][i] != "." and
                self.current_state[0][i] == self.current_state[1][i] and 
                self.current_state[1][i] == self.current_state[2][i]):
                
                return self.current_state[0][i]
    
        for i in range(0, 3):
            if self.current_state[i] == ["X", "X", "X"]:
                return 'X'
            elif self.current_state[i] == ["O", "O", "O"]:
                return 'O'
            
        if (self.current_state[0][0] != "." and 
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            
            return self.current_state[0][0]
        
        if  (self.current_state[0][2] != "." and 
             self.current_state[0][2] == self.current_state[1][1] and
             self.current_state[0][2] == self.current_state[2][0]):
            
            return self.current_state[0][2]
        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == ".":
                    return None

        return "."
    
    def min(self):
        
        min_eval = 2
        
        q_x, q_y = None, None
        
        result = self.is_complete()
        
        if result == "X":
            return (-1, 0, 0)
        elif result == "O":
            return (1, 0, 0)
        elif result == ".":
            return (0, 0, 0)
        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == ".":
                    self.current_state[i][j] = "X"
                    m, max_i, max_j = self.max()
                    
                    if m < min_eval:
                        min_eval = m
                        q_x = i
                        q_y = j
                    self.current_state[i][j] = "."
                        
        return (min_eval, q_x, q_y)                
                      
    def max(self):
        
        max_eval = -2
        
        p_x, p_y = None, None
        
        result = self.is_complete()

        if result == "X":
            return (-1, 0, 0)
        elif result == "O":
            return (1, 0, 0)
        elif result == ".":
            return (0, 0, 0)
        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == ".":

                    self.current_state[i][j] = "O"
                     
                    m, min_i, min_j = self.min()
                    
                    if m > max_eval:
                        max_eval = m
                        p_x = i
                        p_y = j
                    self.current_state[i][j] = "."
                        
        return (max_eval, p_x, p_y)      
                    
    def play(self):
        while True:
            self.draw_board()
            self.winner = self.is_complete()
            
            if self.winner != None:
                if self.winner == 'X':
                    print('The winner is X!')
                elif self.winner == 'O':
                    print('The winner is O!')
                elif self.winner == '.':
                    print("It's a tie!")
                    
                self.init_game()
                return
            
            if self.player_turn == "X":
                
                while True:
                    
                    start = time.time()
                    m, q_x, q_y = self.min()
                    end = time.time()
                    
                    print("Evaluation Time: {}s".format(round(end - start, 5)))
                    print("Evaluated best move = X = {}, Y = {}".format(q_x, q_y))
                    
                    p_x = int(input("Insert the X co-ordinate: "))
                    p_y = int(input("Insert the Y co-ordinate: "))
                    
                    q_x, q_y = p_x, p_y
                    
                    if self.is_valid(p_x, p_y):
                        self.current_state[p_x][p_y] = "X"
                        self.player_turn = "O"
                        break
                    else:
                        print("Error - the move selected is invalid, try again. \n")
            else: 
                m, p_x, p_y = self.max()
                self.current_state[p_x][p_y] = "O"
                self.player_turn = "X"          
            
def main():
      
    game = Game()
    game.play()

if __name__ == "__main__":
    main()