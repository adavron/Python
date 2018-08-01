import random

score = 0

while True:

    num1 = random.randrange(10)
    num2 = random.randrange(10)
    correctAns = num1 + num2

    print ('what is the answer of ' +str(num1) +' + '+str(num2))

    userAns = raw_input('Enter your answer here: ')
    ans = int(userAns)

    if userAns == '':break

    elif ans ==correctAns:
        score +=2
        print ("Thats correct! it's: "+str(correctAns))
        print ("your score is: "+str(score))
    else:
        print ('NOPE, Correct answer is '+str(correctAns))

