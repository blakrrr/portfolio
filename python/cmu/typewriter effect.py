app.stepsPerSecond = 1

text = 'hi the text goes here the ones you want to use for typewriter'
lable = Label('', 200, 200)
for i in text:
    lable.value = lable.value + i
    sleep(0.1)
    
