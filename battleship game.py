
import random                                                                           #import packages
import time

class battleship:                                                                       #class  battleship created
    
    def __init__(self):
        print('**************************************')                                 #define function to make a board
        c=0
        self.d={1:'',2:'',3:'',4:'',5:'',6:'',7:'',                                     #location defined(1-25)
                8:'',9:'',10:'',11:'',12:'',13:'',
                14:'',15:'',16:'',17:'',18:'',
                19:'',20:'',21:'',22:'',
                23:'',24:'',25:''}
        print('\n|-----|-------|-------|-------|------|')                               # to make 5*5 grid
        for each in self.d:
            print(' ',each,end='\t')
            c+=1
            if(c%5==0):
                print('\n|-----|-------|-------|-------|------|')
                c=0
        self.show_grid(self.ship_placed())                                              # called show grid(n)

        
    def show_grid(self,n):                                                              #define function to show board
        c=0
        p=input('Want to check ship location(y/n)')
        print('**************************************')
        if p.lower()!='y':
            SystemExit()
        else:
            print('\n|-----|-------|-------|-------|------|')                           #to show exact location of ship 
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

        
    def ship_placed(self):                                                              #define function to assign random location for ship
        n=random.randint(1,25)                                                          #randint() used
        self.d[n]='SHIP'
        self.guess_the_location(n)                                                      #called guess_the_location(n)
        return n
    
    def guess_the_location(self,n):                                                     #define function for user guess
        g_count=4
        print('\n**************************************')
        prev_guess=[]
        
        while(g_count>0):
            try:                                                                        #try block for user input
                m=int(input("Guess the ship location: " ))
                if m not in range(1,26):
                    raise ValueError
                
            except ValueError:                                                          #except block
                print('Enter valid location(1-25)\n')
                
            else:                                                                       #else block
                if m==n:                                                                #to compare user input with ship location
                    print('\nYeah!!!! You sinked the ship')
                    break
                else:
                    if n%5==0:                                                          #to check user input location is closed to ship
                        if m in (n-5,n-1,n+5):
                            print('You are too close')    
                    elif (n-1)%5==0:
                        if m in (n-5,n+1,n+5,):
                            print('You are too close')
                    else:
                        if m in (n-5,n-1,n+1,n+5):
                            print('You are too close')
                    if m in prev_guess:
                        print("\nLoL!!!\nAre you out of your mind ?")                   #to check prev guesses
                    print('\nOops!!!!               chances left:',g_count-1,'\n')
                    prev_guess.append(m)
                    g_count-=1
        print('**************************************')
        
    def play_again(self):                                                               #define function for next round
        while (True):
            print('**************************************')
            d=input("Do you want to play again(y/n)")
            while d.lower() not in('y','n'):
                d=input("Do you want to play again(y/n)")
            if d.lower()=='n':
                    print('\nThanks for playing.!!!!!Be Happy!!!')
                    time.sleep(2)
                    break
            self.__init__()
            break
        
        
print('**************************************')                                         #introduction block
print('             Battleship')
print('**************************************\n')
print('In Battleship,You have to sink a ship\nwhich is hidden in one of the location')
print('on board given below.\n\nThere are 25 locations.\nYou have 4 chances to guess\nthat location ')


b=battleship()                                                                          #here the game begin
    
