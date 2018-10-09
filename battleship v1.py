#import packages

import random

#class  battleship created

class battleship:
    
#define function to make a board
    
    def __init__(self):
        print('**************************************')
        c=0
        self.d={1:'',2:'',3:'',4:'',5:'',6:'',7:'',
                8:'',9:'',10:'',11:'',12:'',13:'',
                14:'',15:'',16:'',17:'',18:'',
                19:'',20:'',21:'',22:'',
                23:'',24:'',25:''}
        print('\n|-----|-------|-------|-------|------|')
        for each in self.d:
            print(' ',each,end='\t')
            c+=1
            if(c%5==0):
                print('\n|-----|-------|-------|-------|------|')
                c=0
        self.show_grid(self.ship_placed())

#define function to show board
        
    def show_grid(self,n):
        c=0
        p=input('Want to check ship location(y/n)')
        print('**************************************')
        if p.lower()!='y':
            SystemExit()
        else:
            print('\n|-----|-------|-------|-------|------|')
            for each in self.d:
                if each!=n:
                    print(' ',each,end='\t')
                    c+=1
                else:
                    print('',self.d[each],end='\t')
                    c+=1
                if c%5==0:
                    print('\n|-----|-------|-------|-------|------|')
                    c=0
        self.play_again()

#define function to assign random location for ship
        
    def ship_placed(self):
        n=random.randint(1,25)
        self.d[n]='SHIP'
        self.guess_the_location(n)
        return n
    
#define function for user guess
    
    def guess_the_location(self,n):
        g_count=4
        print('\n**************************************')
        prev_guess=[]
        
        while(g_count>0):
            try:
                m=int(input("Guess the ship location: " ))
                if m not in range(1,26):
                    raise ValueError
                
            except ValueError:
                print('Enter valid location(1-25)\n')
                
            else:
                if m==n:
                    print('\nYeah!!!! You sinked the ship')
                    break
                else:
                    if n%5==0:
                        if m in (n-5,n-1,n+5):
                            print('You are too close')    
                    elif (n-1)%5==0:
                        if m in (n-5,n+1,n+5,):
                            print('You are too close')
                    else:
                        if m in (n-5,n-1,n+1,n+5):
                            print('You are too close')
                    if m in prev_guess:
                        print("\nLoL!!!\nAre you out of your mind ?")
                    print('\nOops!!!!               chances left:',g_count-1,'\n')
                    prev_guess.append(m)
                    g_count-=1
        print('**************************************')
         
#define function for next round
        
    def play_again(self):
        while (True):
            print('**************************************')
            d=input("Do you want to play again(y/n)")
            while d.lower() not in('y','n'):
                d=input("Do you want to play again(y/n)")
            if d.lower()=='n':
                    print('Thanks for playing')
                    break
            self.__init__()
            break

#introduction block
        
print('**************************************')
print('             Battleship')
print('**************************************\n')
print('In Battleship,You have to sink a ship\nwhich is hidden in one of the location\non board given below.\n\nThere are 25 locations.\nYou have 4 chances to guess\nthat location ')


#here the game begin

b=battleship()
    
