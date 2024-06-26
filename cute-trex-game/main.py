print('''
*******************************************************************************
              boing         boing         boing              
            e-e           . - .         . - .         . - .          
           (\_/)\       '       `.   ,'       `.   ,'       .        
            `-'\ `--.___,         . .           . .          .       
               '\( ,_.-'                                             
                  \\               "             "            af boy    
                  ^'                                              
*******************************************************************************
''')
print("Hey there little fella! - said the Cute T-rex. - Really glad I found you here! \nI was so entertained just jumping around and dabbing and I forgot I was looking for a dope treasure.😔")
print("Could you please help me? 👉👈")
print("Sure - you said, kinda confused.")
print("The T-rex got really happy and said you had to start the research as soon as possible.") 

first_answer = input('Hop on my back for a ride. - he said. Do you reply "yes" or "no"?\n')
first_answer_lower = first_answer.lower()

if first_answer_lower == "yes":
  second_answer = input('You notice something weird in the back of his head. Type "tell him" or "nope" \n')
  second_answer_lower = second_answer.lower()
  if second_answer_lower == "tell him":
    third_answer = input('Wtf dude, way to start a friendship... he took a shower this morning. Do you say "sorry" or "screw you"?\n')
    third_answer = third_answer.lower()
    if third_answer == "sorry":
      fourth_answer = input("You finally encounter a house in the middle of the woods with 3 doors. One blue, one pink and one lavender. Which colour do you choose?\n")
      fourth_answer = fourth_answer.lower()
      if fourth_answer == "blue":
        print("You chose a door that doesn\'t exist. You blind? Game over, noob.")
      elif fourth_answer == "pink":
        print("Trex's ex was there, got mad and ate you. Not in the naughty way. Game over 💀")
      elif fourth_answer == "lavender":
        print("You found a room full of amethyst crystals 😍 You'll become a guru and hit nirvana. Congrats ❤️")

    elif third_answer == "screw you":
      print("Do I really need to say it?.. fine.. he got mad and had you for lunch 🤡 Game over.")
    
  elif second_answer_lower == "nope":
    print("Karma's a bitch and a meteor fell from space and killed you both 🌑 Game over. ")
  

elif first_answer_lower == "no":
  print("Game over. He got mad and ate you. He's a T-rex, what did you expect?💩")
elif first_answer_lower == "dab":
  print("GG, you won the game. You and the cute T-rex are bffs for life and eventually get rich because of crypto 😎")
