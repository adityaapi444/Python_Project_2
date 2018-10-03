#import Packages

import random
import time

#class created for RPS

class game:
    'This is Rock Paper Scissor game.Rock crushes scissor.Paper covers rock.Scissor cuts Paper.'
    
#initialized with weapon selection
    
    def __init__(self):
        print('**************************************')
        self.choices={1:'Rock',2:'Paper',3:'Scissor'}
        try:
            self.player1=int(input("1: Rock  2: paper 3: Scissor\n\nYour Choice : "))
            if self.player1 not in (1,2,3):
                raise ValueError
        except ValueError:
            print('Choose the right one')
            self.__init__()
        else:
            self.player2=random.choice(list(self.choices.keys()))
            print(self.player2)
            self.rps(self.player1,self.player2)
            
#define func to check the winner

    def rps(self,p1,p2):
        dif=p1-p2
        print('\n************' ,end='');time.sleep(0.3);print('*************', end='');time.sleep(0.2);
        print('******' ,end='');time.sleep(0.1);print('*******', end='\n')
        if dif==0:
            print("Its a Tie!!!\nBoth chose",self.choices[p2])
        elif dif==1 or dif==-2:
            print('Congrats You Won!!!\nOpponent chose',self.choices[p2])
        else:
            print('You lost! Better Luck Next Time!!\nOpponent chose',self.choices[p2])
               
#define func for next round
        
    def play_again(self):
        while (True):
            print('\n**************************************')
            d=input("Do you want to play again(y/n)")
            while d.lower() not in('y','n'):
                d=input("Do you want to play again(y/n)")
            if d.lower()=='n':
                    print('Thanks for playing')
                    break
            self.__init__()

#here the game begin

print('Welcome to the Rock Paper Scissor Game')
g=game()
g.play_again()




            
