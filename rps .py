
import random                                                                                               #import Packages
import getpass
import time

class game:                                                                                                 #class created for RPS
    
    'This is Rock Paper Scissor game.Rock crushes scissor.Paper covers rock.Scissor cuts Paper.'
    
    
    def __init__(self):                                                                                     #initialized with mode selection
        
        print('***************************************')
        self.choices={1:'Rock',2:'Paper',3:'Scissor'}                                                       #choices defined
        try:
            self.mode=int(input("1 : Vs Computer , 2 : Two Player\n\nSelect Mode :"))                       #mode selection
            if self.mode not in (1,2):
                raise ValueError
            
        except ValueError:
            print('Choose the right one')
            self.__init__()
        else:
            self.select_weapon()

                   
    def select_weapon(self):                                                                                #define func. to select weapon
        
        try:
            print('***************************************')
            print('1: Rock  2: paper 3: Scissor\n\n')
            self.player1= int(getpass.getpass(prompt = "For player 1\n\nYour Choice : "))                   #player 1 select weapon
            if self.mode==2:
                self.player2 = int(getpass.getpass(prompt = "\nFor player 2\n\nYour Choice : "))            #player 2 select weapon(when mode = 2)
                if self.player2 not in (1,2,3):
                    raise ValueError
                
            if self.player1 not in (1,2,3):
                raise ValueError
            
        except ValueError:
            print('Choose the right one')
            self.select_weapon()
            
        else:
                if self.mode==1:
                    self.player2=random.choice(list(self.choices.keys()))                                   #player 2(computer) select weapon(when mode=1)
                self.rps(self.player1,self.player2)
            

    def rps(self,p1,p2):                                                                                    #define func. to check the winner
        dif=p1-p2
        print('\n*************' ,end='');time.sleep(0.5);print('*************', end='');time.sleep(0.5);    #sleep() used
        print('******' ,end='');time.sleep(0.5);print('*******', end='\n')
        
        if dif==0:                                                                                          #to check whether match is tie or not 
            print("Its a Tie!!!\nBoth chose",self.choices[p2])
        elif dif==1 or dif==-2:                                                                             #to check  result 
            print('Congrats Player 1 Won!!!\nPlayer 2 chose',self.choices[p2])
        else:
            if self.mode==1:
                print('You Lost!!!Better Luck next Time!!\nComputer chose',self.choices[p2])
            else:
                print('Congrats Player 2 Won!!!\nPlayer 1 chose',self.choices[p1])
                
        self.play_again()
        
        
    def play_again(self):                                                                                   #define func for next round
        
        while (True):
            print('\n***************************************')
            d=input("To play again(y/n) or To Change mode(m)")
            
            while d.lower() not in('y','n','m','yes','no',):
                d=input("To play again(y/n) or To Change mode(m)")
                
            if d.lower()=='n':                                                                              #exit
                    print('\nThanks for playing!!!!Be happy!!')
                    time.sleep(2)
                    break
            if d.lower()=='m':                                                                              #to change the mode
                self.__init__()
                break
            self.select_weapon()                                                                            #to play in same mode
            break


print('Welcome to the Rock Paper Scissor Game')                                                             #here the game begin
print('***************************************')
print('Rock crushes scissor.')
print('          Paper covers rock.')
print('                   Scissor cuts Paper.')
g=game()




            
