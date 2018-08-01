fruit = {"orange":"a sweet, orange, citrus fruit",
         "apple":"good for making cider",
         "lemon":"a sour, yellow",
         "grape":"a small fruit in bunches"}

print fruit


veg = {"cabbage":"this ic green",
       "carrot":"this is yellow",
       "spinach":"this is just spinach"}

print veg


veg.update(fruit)

print veg

fruit.update(veg)
print fruit