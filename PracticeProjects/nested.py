alians = []
for number in range(30):
    new_alian = {'color':'red','speed':'slow','points':5}
    alians.append(new_alian)

total=0
for alian in alians[:5]:
    if alian['color']=='red':
        alian['color'] = 'green'
        alian['speed'] = 'medium'
        alian['points'] = 10
    elif alian['color']=='yellow':
        alian['color'] = 'grey'
        alian['speed'] = 'fast'
        alian['points'] = 15
        




print len(alians)
for alian in alians:
    print alian