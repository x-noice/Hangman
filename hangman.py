# Import the random module to generate a random number
import random
marvel_superheroes = ["IRON MAN","THOR","CAPTAIN AMERICA","HULK","SPIDER MAN","BLACK WIDOW","HAWKEYE","SCARLET WITCH","DOCTOR STRANGE","BLACK PANTHER"]
# Define ASCII art for the win and lose messages, hangman stages, and game credits
won = '''
 __     ______  _    _  __          ______  _   _ _ 
 \\ \\   / / __ \\| |  | | \\ \\        / / __ \\| \\ | | |
  \\ \\_/ / |  | | |  | |  \\ \\  /\\  / / |  | |  \\| | |
   \\   /| |  | | |  | |   \\ \\/  \\/ /| |  | | . ` | |
    | | | |__| | |__| |    \\  /\\  / | |__| | |\\  |_|
    |_|  \\____/ \\____/      \\/  \\/   \\____/|_| \\_(_) 
'''
lost = '''
 __     ______  _    _   _      ____   _____ _______ 
 \\ \\   / / __ \\| |  | | | |    / __ \\ / ____|__   __|
  \\ \\_/ / |  | | |  | | | |   | |  | | (___    | |   
   \\   /| |  | | |  | | | |   | |  | |\\___ \\   | |   
    | | | |__| | |__| | | |___| |__| |____) |  | |   
    |_|  \\____/ \\____/  |______\\____/|_____/   |_|   
'''
hangman_0 = '''
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___  
'''
hangman_1 = '''
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___
'''
hangman_2 = '''
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___  
'''
hangman_3 = '''
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___ 
'''
hangman_4 = '''
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___     
'''
hangman_5 = '''
   _________              
    |/   |                     
    |   (_)                     
    |   /|\\                    
    |    |                       
    |                             
    |                            
    |___      
'''
hangman_6 = '''
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\\                             
    |    |                          
    |   /                            
    |                                  
    |___       
'''
hangman_7 = '''
   ________
    |/   |     
    |   (_)    
    |   /|\\           
    |    |        
    |   / \\        
    |               
    |___   
'''
credit ='''
  __  __           _         ____        
 |  \\/  | __ _  __| | ___   | __ ) _   _ 
 | |\\/| |/ _` |/ _` |/ _ \\  |  _ \\| | | |
 | |  | | (_| | (_| |  __/  | |_) | |_| |
 |_|  |_|\\__,_|\\__,_|\\___|  |____/ \\__, |
                                   |___/ 

     _          _            _               _ _   _           _                  _    _ _ _     
    / \\      __| |_   _  ___| | __ __      _(_) |_| |__     __| | _____   __  ___| | _(_) | |___ 
   / _ \\    / _` | | | |/ __| |/ / \\ \\ /\\ / / | __| '_ \\   / _` |/ _ \\ \\ / / / __| |/ / | | / __|
  / ___ \\  | (_| | |_| | (__|   <   \\ V  V /| | |_| | | | | (_| |  __/\\ V /  \\__ \\   <| | | \\__ \\
 /_/   \\_\\  \\__,_|\\__,_|\\___|_|\\_\\   \\_/\\_/ |_|\\__|_| |_|  \\__,_|\\___| \\_/   |___/_|\\_\\_|_|_|___/                                                                                                                                                      
'''
# Define ASCII art for the hangman game title
hangman = '''
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/                       
'''
# Define a function to explain how to play the hangman game
def how_to_play():
    print(hangman,'\n',credit)
    print('-'*55)
    print('• Guess the word by guessing one letter at a time\n• You have only 7 chances to guess the letter.')
    print('-'*55)
how_to_play()
randInt = random.randint(0,9)
# Get the superhero name as a list of characters and split it into individual characters
hero_name = []
for i in marvel_superheroes[randInt]:
    hero_name.append(i)
chances = 7
chr_entered=[]
# Initialize a list to store the entered superhero name with underscores for unrevealed letters
hero_name_entered = []
# Populate the hero_name_entered list with underscores to represent unrevealed letters
for i in range(len(hero_name)):
    if(hero_name[i]!=' '):
        hero_name_entered.append('_')
    else:
        hero_name_entered.append(' ')
print(hangman_0)
while(chances!=0 and hero_name_entered!=hero_name):
    print(*hero_name_entered,end=' : ')
    input_chr=input()
    # Check if the input is a letter or not
    if input_chr.isalpha() and len(input_chr)==1:
        guessed_chr = input_chr.upper()
        # Check if the input is already entered or not
        if(guessed_chr not in chr_entered):
            chr_entered.append(guessed_chr)
            # Check if the guessed character is in the name
            if(guessed_chr in hero_name):
                # Update the hero_name_entered list to reveal the guessed character
                for i in range(len(hero_name)):
                    if(hero_name[i]==guessed_chr):
                        hero_name_entered[i]=guessed_chr
            # If the guessed character is not in the superhero name, decrement the chances and display the corresponding hangman stage
            elif(guessed_chr not in hero_name):
                chances-=1
                if(chances==6):
                    print(hangman_1)
                    print('Chances left:',chances)
                elif(chances==5):
                    print(hangman_2)
                    print('Chances left:',chances)
                elif(chances==4):
                    print(hangman_3)
                    print('Chances left:',chances)
                elif(chances==3):
                    print(hangman_4)
                    print('Chances left:',chances)
                elif(chances==2):
                    print(hangman_5)
                    print('Chances left:',chances)
                elif(chances==1):
                    print(hangman_6)
                    print('Chances left:',chances)
        elif(guessed_chr in chr_entered):
            print('⚠ You have already entered that letter. Please try again with a different letter.')
    else:
        print('⚠ Please enter a letter.')
# Check if the player won or lost
if(hero_name_entered!=hero_name and chances==0):
    print(hangman_7)
    print(lost)
    print('The word was',marvel_superheroes[randInt])
elif(hero_name_entered==hero_name):
    print(*hero_name_entered)
    print(won)