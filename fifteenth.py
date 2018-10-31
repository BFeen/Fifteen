''' ПЯТНАШКИ '''
import os
import sys
import msvcrt

class Board:
    def __init__(self, value):
        self.board = value
        self.x = 3
        self.y = 3

    def screen(self): # Вывод доски на экран
        print('Игра пятнашки!\t\t\t\tДля новой игры, нажмите R\n')
        for i in self.board:
            for j in i:
                print('\t', j, end=' ')
            print()

    def move(self): # Передвижение фишек
        key = msvcrt.getch()
        if key == b'w':
            if self.x - 1 >= 0:
                self.board[self.x][self.y], self.board[self.x-1][self.y] = self.board[self.x-1][self.y], self.board[self.x][self.y]
                self.x -= 1
        elif key == b'a':
            if self.y - 1 >= 0:
                self.board[self.x][self.y], self.board[self.x][self.y-1] = self.board[self.x][self.y-1], self.board[self.x][self.y]
                self.y -= 1
        elif key == b's':
            if self.x + 1 <= 3:
                self.board[self.x][self.y], self.board[self.x+1][self.y] = self.board[self.x+1][self.y], self.board[self.x][self.y]
                self.x += 1
        elif key == b'd':
            if self.y + 1 <= 3:
                self.board[self.x][self.y], self.board[self.x][self.y+1] = self.board[self.x][self.y+1], self.board[self.x][self.y]
                self.y += 1
        elif key == b'r':
            return False
        return True

    def IsWin(self): # Победа?
        right = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'_']]
        if self.board == right:
            input('Победа!\n')
            return True
        else:
            return False

def main():
    while True:
        os.system('cls')
        b = Board([[15,14,13,12],[11,10,9,8],[7,6,5,4],[3,1,2,'_']])
        b.screen()
        game = True
        while game:
            game = b.move()
            os.system('cls')
            b.screen()
            b.IsWin()


if __name__ == "__main__":
    main()