questions = [
["who is shar rukh khan","WWE wrestlers","plumber","actor","astronaut",3],
["What is the capital of France?", " Berlin", " Madrid", "Paris", " Rome", "3"],
["Which planet is known as the Red Planet?", " Venus",  "Mars", "Jupiter", "Saturn", "2"],
["How many legs does a spider have?", " 6", " 8", "10", " 4", "2"],
["Which animal is known as the King of the Jungle?", " Tiger", " Lion", " Elephant", " Bear", "2"],
["What do bees make?", " Milk", " Silk", " Honey", " Butter", "3"],
["What color are bananas when they are ripe?", " Green", " Yellow", " Red", " Blue", "2"],
["How many days are there in a week?", " 5", " 6", " 7", " 8", "3"],
["Which shape has 3 sides?", " Square", "Circle", " Triangle", " Rectangle", "3"],
["Which fruit is red and often used in pies?", " Banana", " Apple", " Orange", " Grape", "2"],
["Which ocean is the largest?", " Atlantic", " Indian", "Arctic", "Pacific", "4"]
]
prizes =[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000]
i=0
for question in questions:
        print(question[0])
        print(f"a.{question[1]}")
        print(f"b.{question[2]}")
        print(f"c.{question[3]}")
        print(f"d.{question[4]}")
        a=int(input("enter your answer .1 for a,2 for b,3 for c,4 for d\n"
        "")) 
        if(question[5==a]):
                print("correct answer")
        else:
                print(f"Incorrect,the correct answer was {question[5]}") 
                print("Better luck next time!")
                break
        print(f"you won{prizes[1]}")
        i+=1
