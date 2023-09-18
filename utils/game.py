import getpass

class Hangman:
        
        def __init__(self):
            self.lives=5 #variable to initialize lives of gueesr. The parameter changes if gueesr makes mistakes.
            self.correctly_guessed_letters=list()#variable to show up correctly guessed letters
            self.wrongly_guessed_letters=list()#variable to show up wrongly guessed letters
            self.turn_count=0
            self.error_count=0

        def play(self):
                
                """""Enables the user to play the Hangman game. Changes some variables(correctly_guessed_letters,wrongly_guessed_letters,error_count,lives) depending on differnet cases. """
                
                
                
                while True:
                        
                        guess=input("Enter a letter:").upper() 
                        find=False #find variable is using to understand if a letter found.
                        if len(guess)==1 and guess.isalpha()==True :
                                self.turn_count+=1
                                
                                break
                        else:
                                print("please enter a single letter")

                for i in range(0,len(self.word_to_find)) :
                        if guess==self.word_to_find[i]:
                                self.correctly_guessed_letters[i]=guess
                                find=True
                       

                if find ==False:
                        print("sorry") 
                        self.wrongly_guessed_letters.append(guess.upper())
                       
                        self.error_count+=1;
                        self.lives-=1
                else:
                        
                        print("Your guess is right")
                       
                
        def game_over(self,check):
                #The function returs true if the game is over. To understed the lives of the player finished or not.
                if check==0:
                        print("game over")
                        return True
                else:
                        return False
        
        def well_played(self,lst):
                #The function is checking if the player could guess the word and returs true if the player found the word entered by first player.
                if lst==list(self.word_to_find):
                        print("well playyy")
                        return True
               
        def check_input(self):
                #This function is basically trying to get the valid input word which has maximum 8 letters before starting the game.

                input_word_to_find=getpass.getpass(f"First user should enter a word to start playing\nPlease note that you must use words with at most 8 letters.\n ")

                max_length = 8 #maximum number of letters allowed
                while True:
                        if isinstance(input_word_to_find, str) and len(input_word_to_find)<=max_length:
                                 
                                i=0 
                                for i in range(0,len(input_word_to_find)):
                                        
                                        self.correctly_guessed_letters.append('-') 
                                
                                        
                                print("Let's start guessing the letter:")
                                self.word_to_find=str(input_word_to_find).upper()
                                input_word_to_find=""
                                break; return True
                                        
                        else:
                                print("An invalid word entered. Please enter a valid word to find:")
                                self.check_input()
                                return False
                                           
        def start_game(self):
                                #The function which is letting user to start the game checking if the game is over or win.
                                self.check_input()#calling to check if the first player entered a valid word to start playing
                                
                                while self.game_over(self.lives)!=True and self.well_played(self.correctly_guessed_letters)!=True :
                                     
                                        
                                        self.play() #start the hangman!
                                        #print outs for users to inform about the game status
                                        print(f"You made wrong guess {self.error_count} times")
                                        print(f"You made guess for {self.turn_count} times")
                                        print(f"You have {self.lives} lives more")
                                        print(f"The letters guessed CORRECT{self.correctly_guessed_letters}")
                                        print(f"The letters guessed WRONG{self.wrongly_guessed_letters}")
                                        
                                        
                                                
                
                
                
                
                
              
                       
                        
                        

                      
        