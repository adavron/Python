import random

while True:
    print ''                    #prints a blank line
    usersQuestion = raw_input('Ask a question (Return or Enter to quit)')
    if usersQuestion == '':
        break # we are done

    randomAnswer = random.randrange(4) #pick random number

    if randomAnswer == 0:
        print "it is certain"

    elif randomAnswer == 1:
        print "Absolutely"

    elif randomAnswer == 2:
        print "Dont thins so"

    elif randomAnswer == 3:
        print "Can be true"

    elif randomAnswer == 4:
        print "Who cares..."