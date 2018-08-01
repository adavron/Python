confirmed=['lisa','alisa','dan','bob']
unconfirmed=[]

while confirmed:
    user=confirmed.pop()
    print(user+' is being appended')
    unconfirmed.append(user)
    print(unconfirmed)

print(sorted(unconfirmed))

pets=['doc','cat','fish','cat','cat','dew','veq']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)
print(pets)