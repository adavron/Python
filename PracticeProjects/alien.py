alien_0 = {'color':'red','points':5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

print("The alien is "+ alien_0['color'])
alien_0['color']='yellow'
print("The alien is now "+alien_0['color'])

alien_0['speed']='slow'
#alien_0['speed']=raw_input('enter the speed: ')

alien_0['x_position']=0
if alien_0['speed']=='slow':
    x_position=1
elif alien_0['speed']=='medium':
    x_position=2
else:
    x_position=3

alien_0['x_position']=alien_0['x_position']+x_position

print('aliens speed is ' + alien_0['speed'] + ' and '+ str(alien_0['x_position']))

del alien_0['points']
print alien_0

