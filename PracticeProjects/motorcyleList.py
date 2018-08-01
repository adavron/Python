motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('BMW')
print(motorcycles)


sold = 'BMW'
motorcycles.remove(sold)
print(motorcycles)

print(sold.title() + ' has been sold already')

motorcycles.append('mercedes')
print (motorcycles)

sold = 'honda'
del motorcycles[0]
print (sold + ' is gone')
