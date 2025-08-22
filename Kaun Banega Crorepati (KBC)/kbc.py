qustions = [
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai",2],

    ["Who developed Python Programming Language?", "Guido van Rossum" , "Elon Musk" , "Dennis Ritchie" , "Bill Gates", 1],

    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter",3],

    ["Which is the largest ocean in the world?", "Atlantic", "Indian", "Pacific", "Arctic",3],

    ["Who is known as the Father of the Nation (India)?", "Subhash Chandra Bose", "Bhagat Singh", "Mahatma Gandhi", "Jawaharlal Nehru",3],

    ["Which is the national animal of India?", "Elephant", "Tiger", "Lion", "Peacock",2],

    ["Which company created Windows operating system?", "Apple", "Google", "Microsoft", "IBM",3],

    ["Which gas do humans inhale to survive?", "Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen",1],

    ["What is the national currency of India?", "Dollar", "Pound", "Rupee", "Yen",3],

    ["Which is the fastest land animal?", "Lion", "Tiger", "Cheetah", "Horse",3],

    ]

prizes = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 1000000]
money = 0

for i in range(0,len(qustions)):
    question = qustions[i]
    print("\n")
    print(f"Qustion for Rs.{prizes[i]}")
    print(f"\nQ. {question[0]}\n")
    print(f"a.{question[1]}            b.{question[2]}")
    print(f"c.{question[3]}            d.{question[4]}")
    reply = int(input("\nEnter your answer (1-4) or (0 to Quit) : "))

    # Quit condition
    if reply == 0:
        if i==0:
            money =0
            print("You quit the game!")
        else:
            money = prizes[i-1]
            print("You quit the game!")
            break
    
    # Correct answer
    if reply==question[5]:
        print(f"Correct Answer, you have won Rs.{prizes[i]}")
        if i==3:
            money =10000
        elif i==7:
            money = 160000
        elif i==9:
            money = 1000000
    else:
        print("Wrong Answer!")
        if i>=9:
            money = 1000000
        elif i>=7:
            money=160000
        elif i>=3:
            money = 10000
        else:
            money = 0
        break
print(f"Your take home money is {money}")
