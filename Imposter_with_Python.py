''' Welcome to Imposter with Python
            by a beginner '''

import random

print("\n'IMPOSTER' Game with 'PYTHON'")   #_By Manoj Midran M
print(">>> Welcome..! <<<\n")

topics = ["Computer_Hardwares" , "Subjects" , "Stationary_Items" , "Actor" , "Fruits" , "Food_Items"]

#Topics with keys
computer_hardwares = ["Monitor", "Mouse", "Keyboard", "Mike", "Speaker", "Hard drive", "Camera"]
subjects = ["Maths", "Computer Science", "English", "Physics", "Chemistry", "Biology", "History"]
stationary_items = ["Pen", "Scale", "Notebook", "Eraser",  "File"]
actor = ["Tom Holland", "Rajnikanth", "Vijay", "Ranbir Kapoor", "RDJ", "Prabhas"]
fruits = ["Banana", "Apple", "Orange", "Mango", "Water melon"]
food_items = ["Sambar", "Dosa", "Chappathi", "Coffee", "Pizza"]


names = []
no_imposter = 0
word = None
correct_word = ""
imposter_word = ""

def restart():  # Used while restarting
    
    res = random.randint(3,6)
    for _ in range(res):
        print("^_^")
    print('')


while True:         # Infinite loop with break statement
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")            # Display user to enter/exit game
    print("~                                 ~")
    print("~   Enter '1' to START the game   ~")
    print("~   Enter '2' to EXIT the game    ~")
    print("~                                 ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    Enter = int(input(">>> ")) #to start or exit game
    
    if Enter == 1:      # To start the game
        print("\nLet's start the Game >_0\n")
        
        
        while True:
            player_count = int(input('Enter the number of participants: '))     # To get count of players
            
            if player_count <3:         # Condition to check required number of players
                print("\nOops..!\n", "Sorry_! minimum number of participants is: '3'\n")   
                
            elif player_count >=3 and player_count <= 10:
                print(f"\nNumber of players are {player_count}\n")

                while True:
                    no_imposter = int(input("Enter the number of imposter: "))  # To get number of imposter for the game
                    if player_count %2 == 0:
                        max_imposter = (player_count // 2) - 1
                    else:
                        max_imposter = (player_count // 2)
                        
                    
                    if no_imposter <1:          # Condition to check required number of imposters
                        print("Oops..!", "Sorry minimum number of imposter is: '1'\n")
                    
                    elif no_imposter > max_imposter :
                        print("\nOops..!", f"Sorry maximum number of imposter is: '{max_imposter}'\n")
                    else:
                        print(f"\nNumber of imposters is: '{no_imposter}'\n")
                        break
                                                      
                print("Okay... we shall proceed\n")
                break
            
            else:
                print("\nOops..!\n", "Sorry maximum number of participants is: '10'\n")


        for i in range(player_count):       # To ask users to enter each player's name
            Name = input(f"& Enter name of player {i +1}: ")
            names.append(Name)      # To store each player's name in a list called 'names'
        random.shuffle(names)       # Shuffle Name in names for the program to choose imposters in further statements
        
            
        #Shuffle contents within sub topics
        random.shuffle(computer_hardwares)
        random.shuffle(subjects)
        random.shuffle(stationary_items)
        random.shuffle(actor)
        random.shuffle(fruits)
        random.shuffle(food_items)

        topicsd = {"Computer_Hardwares": computer_hardwares , "Subjects": subjects , "Stationary_Items": stationary_items , "Actor": actor , "Fruits": fruits , "Food_Items":food_items}            # A dictionary with keys and 
        
        
        print("\n#####################################")
        print("#")
        print("#   @_Select topic_@  ")                         # Display to user to select topics
        print("#")
        
            
        for index, topic in enumerate(topics):                  # To show user all available topics
            
            print(f"@  Enter '{index + 1}' for {topic}")

        print("#")
        print("#####################################\n")
        
        while True:
            topic_number = int(input(">>> "))               # Make user to choose a topic
            if topic_number >= 1 and topic_number <=6:
                topic_index = topic_number - 1
                break
            else:
                print("Invalid input... Try again.>>>")           

        print("\n>_> The game starts <_< \n")

        imposters = []                              # List to add name of imposters
        non_imposters = []                          # List to add name of non-imposters

        for i in range(no_imposter):                # To make program to choose imposters
            imposters.append(names[i]) 
        for i in range(player_count):
            if names[i] not in imposters:                  # Players other than imposters will be taken
                non_imposters.append(names[i])

        
        random.shuffle(names)       # To shuffle Name in names
        while True:
            for i in names:
                print(f">>> Give the device to '{i}'\n")
            
                while True:
                    verify = int(input(f"Enter '1' if you are '{i}': "))        # To check that the device is with correct player
                    if verify == 1:
                        if i in non_imposters:                  # If the player is non-imposter,
                            word_list = list(topicsd.values())  # Word will take first key in chosen topic which is already suffled
                            word = word_list[topic_index][0]
                            correct_word = word                 # The word taken will be correct word
                            
                        if i in imposters:                      # If the player is imposter,
                            word_list = list(topicsd.values())      # Word will take second key in chosen topic which is already suffled
                            word = word_list[topic_index][1]
                            imposter_word = word                       # The word taken will be imposter word

                            
                        print(f"\n& Your word is: '{word}'\n")      # Show user their word
                        
                        while True:
                            verify1 = int(input("Enter '1' if you have read your word: "))      # To verify that the user read his word
                            if verify1 == 1:
                                for _ in range(50):
                                    print("\n")          # To move fifty lines so that next user will not see key word given to current user
                                break
                            else:
                                print("Invalid input... Try again.>>>")
                        break        
                        
                    else:
                        print("Invalid input... Try again.>>>")
            break
        # Once completed it displays the following
        print("\nEveryone tell a clue about the word you have seen\n to every other participants >_*\n")
                    

        while True:
                verify1 = int(input("Enter '1' if you are ready to move forward: "))
                
                if verify1 == 1:
                    break
                else:
                    print("Invalid input... Try again.>>>")
        
        print("\n& Okay... Guess the imposter and enter their name one by one.\n")
        correct=[]           # To add player's name who told imposter's name correct
        
        for i in names:
            print(f">>> Give the device to '{i}'\n")

            while True:
                if no_imposter == 1:
                    print("Whom do you think the imposter is ?\n")
                elif no_imposter >1:
                    print(f"Enter any one imposter among {no_imposter} imposters\n")
                for index, name in enumerate(names):
                    print(f"@ Enter '{index+1}' for '{name}'")
            
                guess1 = input("\n& Enter the imposter's number: ")             
                guess1 = int(guess1) -1 # To make guess1 as index value
                
                if guess1 >= 0 and guess1 < len(names):        # Check whether correct input is given
                    guess = names[guess1]   # To take current player's guess
                    break
                else:
                    print("Invalid input... Try again.>>>")
            
            if guess in imposters:      # If current player's guess is correct
                print("\n;) You are correct\n")
                print("Don't tell answer to anyone...\n")
                correct.append(i)           # Add current player to list correct
            else:
                print("\n~_~ You are wrong\n")
            while True:
                verify1 = int(input("Enter '1' to move forward: "))
                    
                if verify1 == 1:
                    break
                else:
                    print("Invalid input... Try again.>>>")

                        
            for _ in range(50):     # To move fifty lines so that next user will not the guess given to previous user
                print("\n")

        print(f"\n~ The correct word is: {correct_word}") # Once everyone entered their guess, the program shows correct word, imposter word
        print(f"\n~ The imposter word is: {imposter_word}")

        print("\n& The imposter(s) is/are: ")       # To show who are the imposters
        for i in imposters:
            print(i.title())

        print("")
        print("& Correct answer is said by:")       
        if len(correct) != 0:       
            for i in correct:       # To show whoes guess is correct
                print(i.title())
        else:
            print("None")

        
        print("\n>>> The end...")
        
        print("\nExiting the Game... Good Bye!!!\n")
        print("Have a nice day.!!")
        restart()       # To show before starting the loop again
        
        names = []
        no_imposter = 0
        word = None
        correct_word = ""
        imposter_word = ""
                   
                
    elif Enter == 2:
        print("\nExiting the Game... Good Bye!!!\n")
        print("Have a nice day.!!\n")
        print(">_<")
        break

    else:
        print("Invalid input...\n", "\nRestarting...")
        restart()

        '''
        This program was created on 08.08.2026 
        And still being developed...  @_@
        
        '''

        """

        Once a Bio-Maths Student,
        Now a Coder :)

        I'm just a beginner,
        So my program is simple and has many logic errors,
        Forgive me...

        @_Manoj Midran M
        
        """
        

        
