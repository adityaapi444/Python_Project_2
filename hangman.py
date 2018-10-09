import random
class hangman:

    def __init__(self):
        fo=open('wordbank.txt','r')
        word_bank=fo.read().lower()
        word_list=word_bank.split(',')
        self.n=random.choice(word_list)
        self.n='remove'
        self.split_word=list(self.n)
        self.set_word_letter=set(self.split_word)
        self.user_word=list()
        self.set_user_input=set()
        self.hint_c=1
        print('\t  ',end='')
        for each in self.split_word:
            print('_',end=' ')
            self.user_word.append('_')
        print()
        self.guess_a_letter()

    def hint(self):
        if self.hint_c==0:
            print('\nyou have already used hint')
        while(self.hint_c>0):
            if len(self.set_word_letter-self.set_user_input)<=2:
                print("You can't use hint now\n")
                break
            else:
                self.m=random.choice(list(self.set_word_letter-self.set_user_input))
                self.hint_c-=1
                
    
    #define func for next round
        
    def play_again(self):
        while (True):
            print('*****************************************')
            d=input("Do you want to play again(y/n)")
            while d.lower() not in('y','n'):
                d=input("Do you want to play again(y/n)")
            if d.lower()=='n':
                    print('Thanks for playing')
                    break
            self.__init__()


    def mistakes_hint_count(self):
        if self.m not in self.set_word_letter:
            self.w_count+=1
            print('              mistake(s) :',self.w_count)
        elif self.m in self.prev_guess:
            self.w_count+=1
            print('              mistake(s) :',self.w_count)
        elif self.hint_c==0:
            print('                    Hint :',self.hint_c)
           
    def guess_a_letter(self):
        r_count=0
        self.w_count=0
        self.prev_guess=set()
        for i in range(len(self.split_word)+5):
            try:
                print('\n_________________________________________')
                self.m=input("\nEnter a letter:").lower()
                if (self.m.isalpha()!=True and self.m!='*') or len(self.m)!=1:
                    raise ValueError
                if self.m=='*':
                    self.hint()
            except ValueError :
                print('\nYou missed one chance')
                print('enter single alphabetic char only')

            if self.m in self.prev_guess:
                print('\nYou are out of you mind\nYou repeated the same guess')
            for each in self.split_word:
                r_count+=1
                if each==self.m:
                    self.set_user_input.add(each)
                    self.user_word[r_count-1]=self.m
            r_count=0
            
            for each in self.user_word:
                print(each,end=' ')
            
            if self.user_word==self.split_word:
                print('\n\nYou have survived')
                break
            self.mistakes_hint_count()
            self.prev_guess.add(self.m)
            if self.w_count==7:
                print('_________________________________________')
                print('\nYou got hanged')
                print('   ____')
                print('  |    |   ')   
                print('  |    o  ')    
                print('  |   /|\ ')
                print('  |    |')     
                print('  |   / \ ')
                print('  |')
                print(' _|__________\n')
                print("The word is '",self.n,"'")
                break
        self.play_again()            
print('*****************************************')
print('         Hangman(Word Game)')
print('*****************************************')
print('In hangman, You have to recognize a word.')
print('Your 7 mistakes are forgiven\nIf you could not racognize then you will\nget hanged\n')
print("No.of Hint:1\nType '*' instead of letter to get hint")
print('*****************************************')
h=hangman()
h.play_again()
