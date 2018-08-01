user_0={
    'username':'adavronov',
    'first':'azizbek',
    'last':'davronov'
}

print (user_0)

for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: "+ value)

favorite={
    'jen':'python',
    'hana':'c',
    'sarah':'ruby',
    'phil':'java'
}

print favorite

friend=['jen','phil']

for name in favorite.keys():
    print(name.title())

    if name in friend:
        print('Hi dear '+ name.title()+' I see your favorite langiage is '+ favorite[name].upper())

for item in favorite.items():
    print (item)

for name in sorted(favorite.keys()):
    print name.title()
