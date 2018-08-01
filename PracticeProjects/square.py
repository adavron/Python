
def square(num):
    sq = num * num
    return sq

userNum = raw_input('Enter a number: ')
userNum = float(userNum)
squareNum = square(userNum)
print 'The square of ',userNum, 'is ', squareNum