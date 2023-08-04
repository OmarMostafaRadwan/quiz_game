print ("hi wecome to my quiz game")

playing = input("do you want to play y or n ? ")
if playing != "y" :
    quit()
print("ok lets start")

your_score = 0

answer1 = input("what is my name? ")
if answer1 == "omar":
    print("correct")
    your_score += 1
    print("your score is", your_score)
       
else:
    print ("incorrect")

print("------------------")

answer2 = input("what is my brother name? ")
if answer2 == "ali":
    print("correct")
    your_score += 1
    print("your score is", your_score)
    
    
else:
    print ("incorrect")

    