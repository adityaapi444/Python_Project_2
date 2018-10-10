
import random                                                                                                       #import packages
import time

class hangman:                                                                                                      #create a class hangman 
    
    def __init__(self):                                                                                             #define func. to pick random word
        fo=open('wordbank.txt','r')
        word_bank=fo.read()                                                                                         #file 'wordbank.txt' read
        word_list=word_bank.lower().split(',')                                                                      #word get splited(',')
        random.shuffle(word_list)                                                                                   #random.shuffle() used
        self.n=random.choice(word_list)                                                                             #choice() used
        self.split_word=list(self.n)                                                                                #letters get seperated
        self.set_word_letter=set(self.split_word)
        self.user_word=list()                                                                                       #list created for user_input
        self.set_user_input=set()                                                                                   #set created for guessed letter
        self.hint_c=round(len(self.split_word)*0.25)                                                                #no.of hints calculated based on len of word
        print('\t\t\t  ',end='')
        
        for each in self.split_word:
            print('_',end=' ')
            self.user_word.append('_')
        print()
        self.guess_a_letter()
        
    def hint(self):                                                                                                 #define func. for hint
        if self.hint_c==0:
            print('\nHints are over')
        while(self.hint_c>0):
            self.m=random.choice(list(self.set_word_letter-self.set_user_input))                                    #hint given to user 
            self.hint_c-=1                                                                                          #hint decreased to 1
            break;
        
    def play_again(self):                                                                                           #define func. for next round
        while (True):
            print('********************************************************************************')
            d=input("Do you want to play again(y/n)")
            print()
            while d.lower() not in('y','n'):
                d=input("Do you want to play again(y/n)")
            if d.lower()=='n':
                    print('\nThanks for playing!!!!!Be Happy!!')
                    time.sleep(2)
                    break
            self.__init__()
            break
            
            
    def mistakes_count(self):                                                                                       #define func. to count mistakes
        if self.m not in self.set_word_letter:
            self.w_count+=1                                                                                         #mistakes count increased to 1
        elif self.m in self.prev_guess:
            self.w_count+=1                                                                                         #mistakes count increased to 1

            
    def guess_a_letter(self):                                                                                       #definr func. to guess letter
        r_count=0                                                                                                   #r_count used in line no.91
        self.w_count=0
        self.prev_guess=set()
        for i in range(len(self.split_word)+6):
            try:                                                                                                    #try block
                
                print('________________________________________________________________________________')
                print('                                                                   Hint(s) :',self.hint_c)
                self.m=input("\nEnter a letter:").lower()
                
                if (self.m.isalpha()!=True and self.m!='*') or len(self.m)!=1:                                      #user input validation
                    raise ValueError
                if self.m=='*':                                                                                     #called hint()
                    self.hint()
                    
            except ValueError :                                                                                     #except block
                print('\nYou missed one chance')
                print('Enter single alphabetic char only')

            if self.m in self.prev_guess:       
                print('\nYou are out of you mind\nYou repeated the same guess')
            print()
            for each in self.split_word:                                                                            #process of guessing letter started
                r_count+=1
                if each==self.m:
                    self.set_user_input.add(each)                                                                   #letter added to set_user_input 
                    self.user_word[r_count-1]=self.m                                                                #valid letter placed to appropriate location
            r_count=0
            
            for each in self.user_word:                                                                             #user_word get printed
                print(each,end=' ')
            
            if self.user_word==self.split_word:
                print('\n\nCongrats!!!!\nYou have survived!!!!')                                                    #checking user_word with the original 
                break
            
            self.mistakes_count()
            print('\n\n                                                                 mistake(s):',self.w_count)  #to display no. of mistakes
            
            self.prev_guess.add(self.m)
            print('\nPrev Guess : ',self.prev_guess)
            if self.w_count==7:                                                                                     #to check no. of mistakes==7
                print('________________________________________________________________________________')
                print('\nYou got hanged')
                print('   _________')
                print('  | /  |   ')   
                print('  |/   o  ')    
                print('  |   /|\ ')
                print('  |    |')     
                print('  |   / \ ')
                print('  |')
                print(' _|__________\n')
                print("The word is '",self.n,"'")
                break
            
        self.play_again()                                                                                           #called play_again()
        
                                                                                                                    #introduction block
        
print('********************************************************************************')
print('                             Hangman(Word Game)')
print('********************************************************************************')
print('In hangman, You have to recognize a word.')
print('\nIf you could not recognize then you will get hanged\n\nYour 6 mistakes will be forgiven')
print("\nNote : For Hint type '*' instead of letter")
print('********************************************************************************')

h=hangman()                                                                                                         #here the game begin


