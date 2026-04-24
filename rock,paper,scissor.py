"""
work flow of this code 
input from user( rock, paper,scissor)
computer can choose randomly
cases:
user choose rock:
rock-rock=tie
rock-paper= computer win
rock-scissor= you win"""

import random
item_list=["rock","paper","scissor"]
user_choice= input("enter the move  of user :")
comp_choice=random.choices(item_list)
print(f"your choice is:{user_choice} \n computer choice is:{comp_choice}")

if user_choice==comp_choice:
    print("both are same = tie")

elif user_choice=="rock":
        if comp_choice=="paper":
              print("paper cover rock= computer win")
        else:
              print("rock brake scissor= you win")

elif   user_choice=="paper":
        if comp_choice=="rock":
              print("paper cover rock= you win")
        else:
              ("scissor cut the paper= computer  win ")    

elif user_choice=="scissor":
         if comp_choice=="paper":
                print("scissor cut the paper=you win")

         else:
               print(" rock broke the scissor=computer win")
              
      
