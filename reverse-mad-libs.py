#create a title
print "\t\t\t ----------------"
print "\t\t\t Coffee Trivia!"

print "\t\t\t Wake up and test your coffee knowledge!"
print "\t\t\t ----------------"
print("Get ready to fill in the blanks! How hard would you like this to be?")

#game modes
easy = "\n \n \n The best part of waking up, is ___1___ in your cup! \n An Americano is ___2___ and ___3___. \n Chocolate is added to coffee to make it a ___4___. \n \n \n" 
med = "\n \n \n Blue Mountain coffee comes from ___1___. \n Kona coffee comes from ___2___. \n Coffee is the ___3___ largest traded commodity in the world. Oil is the first.  \n Starbucks headquarters is in the city of ___4___. \n"
hard = "\n \n \n ___1___ is the country that exports the most coffee.\n The word coffee evolved from the ___2___ word 'Qahwa' meaning wine of the bean. \n The worlds most expensive coffee is from indonesia and is called ___3___. \n There are two major varieties of coffee plants, Arabica and ___4___. \n" 

easy_answers = ['Folgers', 'espresso', 'water', 'mocha']
easy_answers2 = ['Folgers', 'water', 'espresso', 'mocha']
med_answers = ['Jamaica', 'Hawaii', 'second', 'Seattle'  ]
hard_answers = ['Brazil', 'arabic' 'Kopi Luwak' 'robusta']
#just appending user inputs into this
user_answers = []

#ok... lots of repitition here but I couldnt figure out how to make this a function... Actually not even sure if I need a while loop. was thinking of adding a play again so thats why I thought it might be worthwhile.
while True:
  difficulty = raw_input("Type: easy, medium, or hard: ")  
  if difficulty == "easy":
    print easy
    blank1 = raw_input("Enter answer 1 ")
    blank1 = user_answers.append(blank1)
    blank2 = raw_input("Enter answer 2 ")
    blank2 = user_answers.append(blank2)
    blank3 = raw_input("Enter answer 3 ")
    blank3 = user_answers.append(blank3)
    blank4 = raw_input("Enter answer 4 ")
    blank4 = user_answers.append(blank4)
    break
  elif difficulty == "medium":
    print med
    blank1 = raw_input("Enter answer 1 ")
    blank1 = user_answers.append(blank1)
    blank2 = raw_input("Enter answer 2 ")
    blank2 = user_answers.append(blank2)
    blank3 = raw_input("Enter answer 3 ")
    blank3 = user_answers.append(blank3)
    blank4 = raw_input("Enter answer 4 ")
    blank4 = user_answers.append(blank4)
    break
  elif difficulty == "hard":
    print hard
    blank1 = raw_input("Enter answer 1 ")
    blank1 = user_answers.append(blank1)
    blank2 = raw_input("Enter answer 2 ")
    blank2 = user_answers.append(blank2)
    blank3 = raw_input("Enter answer 3 ")
    blank3 = user_answers.append(blank3)
    blank4 = raw_input("Enter answer 4 ")
    blank4 = user_answers.append(blank4)
    break
  else:
    print("Hey! Just choose a difficulty!")      

# I wanted to avoid repeating here as well but i got errors when i tried to chain all the if, elif statements. Also need to figure out a way to match one answer at a time. played with split but couldnt get it... ill keep trying.
while True:
  if user_answers == easy_answers:
    print ("YOU WIN!") 
  elif user_answers == easy_answers2:
    print ("YOU WIN!") 
  elif user_answers == med_answers:
    print ("YOU WIN!") 
  elif user_answers == hard_answers:
    print ("YOU WIN!") 
  else:
      print("You got some wrong, but which ones? If I was a better coder, I could tell you that. try again\n\n")
  break  

