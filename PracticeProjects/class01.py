class kido(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

bigkido = kido("bigkido", 16)
print bigkido.name
print bigkido.price
print bigkido.on

kenwood = kido("kenwood", 2)
print kido.switch_on(kenwood)

print kenwood.on
