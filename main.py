import random 


scorce_cp = 0
score_user = 0
runs_user = 0
runs_cp = 0
bb = ["ball","bat"]


list = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth", "Nineteenth", "Twentieth", "Twentifirst", "Twentisecond", "Twentithird", "Twentifourth", "Twentififth", "Twentisixth", "Twentiseventh", "Twentieightth", "Twentininth", "Thirtieth" ]



choice_user = str(input("Choose btwn even or odd: "))
while choice_user != ("even" or "odd"):
  print("Please enter a valid input!")
  choice_user = str(input("Choose btwn even or odd: "))
  if choice_user == ("even" or "odd"):
     break

if choice_user == "even":
  choice_cp = "odd"
elif choice_user == "odd":
  choice_cp = "even"
  

        
num_user = int(input("Choose a number from 1 to 6: "))
num_cp = random.randint(1,6)
print(f"Computer chose {num_cp}")
toss = (num_user + num_cp)%2




def user_bat():
  runs_user = 0
  for i in range(0,100):
    score_user = int(input(f"{list[i]} ball: "))
    score_cp = random.randint(1,6)
    print(score_cp)
    i += 1
    runs_user = runs_user + score_user
    print(f"Total runs scored by you until now: {runs_user}")
    if score_user == score_cp:
      print("Outs that!\n")    
      print("    ¯\_(ツ)_/¯\n") 
      
      global total_user
      total_user = runs_user 
      break
      


def user_ball():
  runs_cp = 0
  for j in range(0,100):
    score_user = int(input(f"{list[j]} ball: "))
    score_cp = random.randint(1,6)
    print(f"Computer scored {score_cp} runs!")
    j += 1
    runs_cp = runs_cp + score_cp
    print(runs_cp)
    if (score_cp == score_user):
      print("Clean bold\n")
      print("   (≧▽≦)\n")
      global total_cp 
      total_cp = runs_cp
      break
  


def user_win():
    play = str(input("Choose bat or ball: "))
    if play == "bat":
      user_bat()
      print("-"*28)
      print(f"| You scored total {total_user} runs |")
      print("-"*28)
      print("Now its your turn to ball \n")
      user_ball()
      print("-"*44)
      print(f"|  Computer scored total {total_cp} runs! (ー_ー;)  |")
      print("-"*44)

    elif play == "ball":
      user_ball()
      print("-"*45)
      print(f"|  Computer scored total {total_cp} runs! (ー_ー;)  |")
      print("-"*45)
      print("Now its your turn to bat\n")
      user_bat()
      print("-"*44)
      print(f"|  You scored total {total_user} runs ＼（^０＾）／  |")
      print("-"*44)



def cp_win():
  play = random.choice(bb)
  if play == "ball":
    print("Computer chose to ball")
    user_bat()
    print("-"*44)
    print(f"|  You scored total {total_user} runs ＼（^０＾）／  |")
    print("-"*44)
    print("Now its your turn to ball\n")
    user_ball()
    print("-"*45)
    print(f"|  Computer scored total {total_cp} runs! (ー_ー;)  |")
    print("-"*45)
  elif play == "bat":
    print("Computer chose to bat")
    user_ball()
    print("-"*45)
    print(f"|  Computer scored total {total_cp} runs! (ー_ー;)  |")
    print("-"*45)
    print("Now its your turn to bat\n")
    user_bat()
    print("-"*44)
    print(f"|  You scored total {total_user} runs ＼（^０＾）／  |")
    print("-"*44)
    

  
 

if choice_user == "even":
  choice_cp == "odd"
  if toss == 0:
    print("You won the toss!")
    user_win()
  elif toss != 0:
    print("Computer won the toss")
    cp_win()
    

elif choice_user == "odd":
  choice_cp == "even"
  if toss != 0:
    print("You won the toss!")
    user_win()
  elif toss == 0:
    print("Computer won the toss!")
    cp_win()
      

    
if total_cp > total_user:
  diff = total_cp - total_user
  print(f"Computer won by scoring {diff} runs more than you! (T^T)")

elif total_user > total_cp:
  diff = total_user - total_cp
  print(f"You won by scoring {diff} more runs than the computer! ᕙ(⇀‸↼‶)ᕗ")






'''
even -> toss won -> check even or odd-> even -> bat or ball -> bat -> out -> ball -> over✅
even -> toss won -> check even or odd-> even -> bat or ball -> ball -> out -> bat -> over✅
even -> toss lost -> check even or odd-> odd -> by default bat or ball ->  got bat -> out -> ball -> over✅
even -> toss lost -> check even or odd-> odd -> by default bat or ball ->  got ball -> out -> bat -> over✅


odd -> toss won -> check even or odd-> odd -> bat or ball -> bat -> out -> ball -> over ✅
odd -> toss won -> check even or odd-> odd -> bat or ball -> ball -> out -> bat -> over✅
odd -> toss lost -> check even or odd-> even -> by default bat or ball ->  got bat -> out -> ball -> over✅
odd -> toss lost -> check even or odd-> even -> by default bat or ball ->  got ball -> out -> bat -> over✅
'''

#Trash Code
'''
choice_user = str(input("Choose btwn even or odd: "))
if choice_user == "even":
  choice_cp = "odd"
elif choice_user == "odd":
  choice_cp = "even"
'''

'''
elif (choice_user != "even" or choice_user != "odd"):
  for i in range(1,100):
    if (choice_user != "even" or choice_user != "odd"):
      choice_user = str(input("Choose btwn even or odd: "))
      if flag:
        break
      
  while(choice_user != "even" or choice_user != "odd"):
   choice_user = str(input("Choose btwn even or odd: "))
'''
