# Rock Paper Scissors:

import random
import string
import os

print("Welcome to the rock paper scissors game, good luck!") 

possible_outcomes = ["rock", "paper", "scissors"] 

while True: 
  user_inputs = input("Please choose now, Rock (R), Paper (P) or Scissors (S): ") 
  
  computer_input = random.choice(possible_outcomes) 
  
  # user_inputs.lower() # Not functioning properly? 
  
  print("the computer chose:", computer_input)
  
  if user_inputs == "r" and computer_input == "rock":
    print("It is a tie!") 
  elif user_inputs == "r" and computer_input == "paper":
    print("The computer wins!")
  elif user_inputs == "r" and computer_input == "scissors":
    print("You won!")
  elif user_inputs == "p" and computer_input == "rock":
    print("You win!") 
  elif user_inputs == "p" and computer_input == "paper":
    print("It is a tie!")
  elif user_inputs == "p" and computer_input == "scissors":
    print("The computer wins!") 
  elif user_inputs == "s" and computer_input == "rock":
    print("The computer wins!")
  elif user_inputs == "s" and computer_input == "paper":
    print("You win!")
  elif user_inputs == "s" and computer_input == "scissors":
    print("It is a tie!")
  elif user_inputs == "R" and computer_input == "rock":
    print("It is a tie!") 
  elif user_inputs == "R" and computer_input == "paper":
    print("The computer wins!")
  elif user_inputs == "R" and computer_input == "scissors":
    print("You won!")
  elif user_inputs == "P" and computer_input == "rock":
    print("You win!") 
  elif user_inputs == "P" and computer_input == "paper":
    print("It is a tie!")
  elif user_inputs == "P" and computer_input == "scissors":
    print("The computer wins!") 
  elif user_inputs == "S" and computer_input == "rock":
    print("The computer wins!")
  elif user_inputs == "S" and computer_input == "paper":
    print("You win!")
  elif user_inputs == "S" and computer_input == "scissors":
    print("It is a tie!")

  go_again = input("Do you want to play again (Y/N)? ") 

  if go_again == "n" or go_again == "N":
    print("Okay, see you next time!")
    break 
    
  # os.system('cls') # Not working?
  
