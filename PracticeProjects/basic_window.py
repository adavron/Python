def basic_window(width, height, font='TNR'):
    print(width,height,font)

text = 'This is text \n And this is the second line of this text'
saveFile = open('textfile','w')
saveFile.write(text)
saveFile.close()
