#created in may of 2023
#playable version at: https://academy.cs.cmu.edu/sharing/floralWhiteSnake7579/

# this is an autoscrolling game in which the character you play as jumps over walls to achieve a new high score, with the walls changing each time.
# additionally, there is a plethora (7) of achievements, each that are able to be acquired through achieving better or sometimes worse scores.
# here is a photo of a sucessful 50 points, showing that all achievements are possible: https://github.com/Blakey546/beakfestcomics.github.io/blob/main/Screenshot%202023-05-12%2010.33.02%20AM.png?raw=true
app.stepCount = 0
plr = Group(Rect(175,175,20,20, fill='white', border='black', borderWidth=3), Line(180,195,180,200, lineWidth=3), Line(190,195,190,200, lineWidth=3),
Rect(182,180,2.5,2.5), Rect(187.5,180,2.5,2.5))
plr.dy = 0
wall =Rect(400,160,20,48, fill='red')
ground = Rect(0,200,400,200)
app.jump = False
collison1= Rect(-25,0,25,400)
collison2 = Rect(400,0,25,400)
score = Label(0,350,25, size=35)
pause = Label('Press P to Pause',75,380, fill='white',size = 16)
ribbon = Image('cmu://588513/22535966/clipboard.png', 5, 5)
achievements = Rect(0,0,400,400, fill='grey', opacity=75)
a1 = Group(Label('Just Getting Started', 100,50), Label('Sucessfully survive 5 walls.', 300, 50))
a2 = Group(Label('Big Number 10', 100,100), Label('Sucessfully survive 10 walls.', 300, 100))
a3 = Group(Label('Give it Up for Day 15!', 100,150), Label('Sucessfully survive 15 walls.', 300, 150))
a4 = Group(Label('Your Successes Can Drink Now!', 100,200), Label('Sucessfully survive 21 walls.', 300, 200))
a5 = Group(Label("50, That's Some Dedication!", 100,250), Label('Sucessfully survive 50 walls.', 300, 250))
a6 = Group(Label('You tried..', 100,300), Label('Lose with a score less than 5.', 300, 300)) 
a7 = Group(Label("You can't win by doing nothing..", 100,350), Label('Try to win without moving.', 300, 350))
achieved1 = Group(Rect(100,0,200,50, fill=gradient('lime', 'lime', 'lime', rgb(0,200,0), start='top'), opacity=50), Label('Achievement Gotten!', 160,10))
achieved2 = Label("TEST", 200, 35)
app.keyPressCount = 0
def achievementsVisible(boolean):
    achievements.visible=boolean
    a1.visible=boolean
    a2.visible=boolean
    a3.visible=boolean
    a4.visible=boolean
    a5.visible=boolean
    a6.visible=boolean
    a7.visible=boolean
def achieved(theThing):
    achieved1.visible=True
    achieved2.visible=True
    achieved2.value=theThing
achievementsVisible(False)
gameover = Group(Rect(0,0,400,400, fill='red', opacity = 75), Label('Game Over', 200,200, size=50), Label('Press R to Retry', 200, 250, size=25))
gameover.visible=False
app.pause = False
app.death = False
app.clickCount = 0
achieved1.visible=False
achieved2.visible=False
def onKeyHold(keys):
    if app.pause == False and app.death == False:
        if 'left' in keys:
            plr.centerX -= 3
            app.keyPressCount += 1
        elif 'right' in keys:
            plr.centerX += 3
            app.keyPressCount += 1
        if plr.centerX == 250:
            plr.centerX = 250
def onKeyPress(key):
    if app.death == False:
        if key == 'up' and app.jump == False:
            app.jump = True
            plr.dy -= 5
            app.keyPressCount += 1
        if key == 'p':
            if app.pause==False:
                app.pause=True
            else:
                app.pause=False
    if key == 'r' and app.death == True:
        app.death = False
        app.pause = False
        score.value = 0
        gameover.visible=False
        achievementsVisible(False)
        wall.left = 400
        plr.centerX = 185
        app.keyPressCount = 0
        
def onStep():
    app.stepCount += 1
    if app.stepCount % 100 == 0:
        achieved1.visible=False
        achieved2.visible=False
    if app.pause == False and app.death == False:
        if app.jump == True:
            plr.dy += 0.25
            plr.centerY += plr.dy
        if plr.hitsShape(ground):
            plr.dy = 0
            app.jump=False
        if plr.hitsShape(collison1):
            plr.centerX +=3
        if plr.hitsShape(collison2):
            plr.centerX -=3
        if wall.left <= 400 and wall.left >=-65:
            wall.left -= 5
        else:
            wall.left = 400
            wall.top = randrange(155,195)
            score.value += 1
        if plr.hitsShape(wall):
            gameover.visible=True
            app.death = True
            if score.value <= 5:
                a6.fill='lime'
            if app.keyPressCount == 0: 
                a7.fill='lime'
                achieved("You can't win by doing nothing..")
    if score.value == 5:
        a1.fill='lime'
        if app.pause==False:   
            achieved('Just Getting Started')     
    if score.value == 10:
        a2.fill='lime'
        if app.pause==False:   
            achieved("Big Number 10")
    if score.value == 15:
        a3.fill='lime'
        if app.pause==False:   
            achieved("Give it Up for Day 15!")
    if score.value == 21:
        a4.fill='lime'
        if app.pause==False:   
            achieved('Your Successes Can Drink Now!')
    if score.value == 50:
        a5.fill='lime'
        if app.pause==False:   
            achieved('You tried..!')
def onMousePress(mouseX,mouseY):
    if ribbon.contains(mouseX,mouseY):
        app.clickCount += 1
        if app.clickCount % 2 == 0:
            app.pause = False
            achievementsVisible(False)
            if app.death==True:
                gameover.visible=True
        if not app.clickCount % 2 == 0:
            app.pause=True
            achievementsVisible(True)
            achieved1.visible=False
            achieved2.visible=False
            if gameover.visible == True:
                gameover.visible=False
