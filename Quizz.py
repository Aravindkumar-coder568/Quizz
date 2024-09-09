print("Welcome to Quizz ....Challange ")

player=input("Are you want to play the quiz ?:")
player=player.lower()

if player!="yes":
    quit()
print("Let's GO!.... ")

score=0

#Q1
question=input("Who is principle of RTC? ")
question=question.lower()
if question=="Nagaraj":
    print("correct")
    score+=10
else:
    print("incorrect")
    

#Q2    
question=input("Abbreation of RBI ")
question=question.lower()
if question=="reserve bank of india":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q3
question=input("who is Tamil Nadu Chief misister? ")
question=question.lower()
if question=="Stalin":
    print("correct")
    score+=10
else:
    print("incorrect")



#Q4 
question=input("What is the national flower of India? ")
question=question.lower()
if question=="lotus":
    print("correct")
    score+=10
else:
    print("incorrect")



#Q5
question=input("What is the national sport of India? ")
question=question.lower()
if question=="hockey":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q6
question=input("What is the least developed state in India? ")
question=question.lower()
if question=="bihar":
    print("correct")
    score+=10
else:
    print("incorrect")
    

#Q7    
question=input("which is richest state in india?")
question=question.lower()
if question=="maharashtra":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q8
question=input("What is the longest river in India? ")
question=question.lower()
if question=="indus river":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q9
question=input("What is the national bird of India? ")
question=question.lower()
if question=="peacock":
    print("correct")
    score+=10
else:
    print("incorrect")
    
    
    
#Q10
question=input("What is the most populous state in India? ")
question=question.lower()
if question=="Tamil Nadu":
    print("correct")
    score+=10
else:
    print("incorrect")


print("Your score is:",score,"/ 100")

print()
print()

print("-----------THANK YOU FOR PLAY THIS QUIZZ...-------------")
