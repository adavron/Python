class Restaurant(object):
    """this is restaurant class"""
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def open(self):
        print (self.name + ' is open')


buk = Restaurant('buka','italian')

print buk.name
print buk.type
buk.open()

susi = Restaurant('susi', 'bar')
susi.open()


