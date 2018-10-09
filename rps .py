#import Packages

import random
import getpass
import time


#class created for RPS

class game:
    'This is Rock Paper Scissor game.Rock crushes scissor.Paper covers rock.Scissor cuts Paper.'
    
#initialized with mode selection
    
    def __init__(self):
        print('***************************************')
        self.choices={1:'Rock',2:'Paper',3:'Scissor'}
        try:
            self.mode=int(input("1 : Vs Computer , 2 : Two Player\n\nSelect Mode :"))
            if self.mode not in (1,2):
                raise ValueError
            
        except ValueError:
            print('Choose the right one')
            self.__init__()
        else:
            self.select_weapon()
            
#define function to select weapon
            
    def select_weapon(self):
        try:
            print('***************************************')
            print('1: Rock  2: paper 3: Scissor\n\n')
            self.player1= int(getpass.getpass(prompt = "For player 1\n\nYour Choice : "))
            if self.mode==2:
                self.player2 = int(getpass.getpass(prompt = "\nFor player 2\n\nYour Choice : "))
                if self.player2 not in (1,2,3):
                    raise ValueError
            if self.player1 not in (1,2,3):
                raise ValueError
        except ValueError:
            print('Choose the right one')
            self.select_weapon()
        else:
                if self.mode==1:
                    self.player2=random.choice(list(self.choices.keys()))
                self.rps(self.player1,self.player2)
            
#define func to check the winner

    def rps(self,p1,p2):
        dif=p1-p2
        print('\n*************' ,end='');time.sleep(0.5);print('*************', end='');time.sleep(0.5);
        print('******' ,end='');time.sleep(0.5);print('*******', end='\n')
        if dif==0:
            print("Its a Tie!!!\nBoth chose",self.choices[p2])
        elif dif==1 or dif==-2:
            print('Congrats Player 1 Won!!!\nPlayer 2 chose',self.choices[p2])
        else:
            if self.mode==1:
                print('You Lost!!!Better Luck next Time!!\nComputer chose',self.choices[p2])
            else:
                print('Congrats Player 2 Won!!!\nPlayer 1 chose',self.choices[p1])
        self.play_again()
        
#define func for next round
        
    def play_again(self):
        while (True):
            print('\n***************************************')
            d=input("To play again(y/n) or To Change mode(m)")
            while d.lower() not in('y','n','m','yes','no',):
                d=input("To play again(y/n) orTo Change mode(m)")
            if d.lower()=='n':
                    print('\nThanks for playing.\tBe happy')
                    time.sleep(2)
                    break
            if d.lower()=='m':
                self.__init__()
                break
            self.select_weapon()
            break

#here the game begin

print('Welcome to the Rock Paper Scissor Game')
print('***************************************')
print('Rock crushes scissor.')
print('          Paper covers rock.')
print('                   Scissor cuts Paper.')
g=game()




            
