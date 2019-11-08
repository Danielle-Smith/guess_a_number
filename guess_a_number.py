import random
random_choice = random.randint(0,10)


user_choice = input("Can you guess the number I'm thinking of? 1-10: ")


while int(user_choice) != (random_choice):
        print('Try again')
        user_choice = input("Can you guess the number I'm thinking of? 1-10: ")

if int(user_choice) == int(random_choice):
        print('Correct!')
        
        


    

    
      




    
