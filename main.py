import random

app.background=gradient("midnightBlue",'Purple',start='top')

Label('Master Your 6 Times Table!',200,35,size=28,bold=True,fill='coral')

app.allAnswers=[6,12,18,24,30,36,42,48,54,60]
app.questionNumber=0
app.wrongClicks=0
app.totalRight=0
app.scoreHistory=[]


app.quizShapes=Group()

mainBox=Rect(20,100,360,200,fill='lavender',border='indigo',borderWidth=3)
questionText=Label('6 x 1 = ',210,150,bold=True,fill='indigo',size=24)
helpText=Label("Look at the question then click on the right answer:",200,120,bold=True,size=13,fill='darkslateGray')


box1=Group(Rect(50,175,300,32,fill='plum',border='purple'),Label('6',200,191,size=18,bold=True))
box2=Group(Rect(50,215,300,32,fill='plum',border='purple'),Label("12",200,231,size=18,bold=True))
box3=Group(Rect(50,255,300,32,fill='plum',border='purple'),Label("18",200,271,size=18,bold=True))


app.quizShapes.add(mainBox,questionText,helpText,box1,box2,box3)
app.buttonsList=[box1,box2,box3]

nextArrow=Polygon(355,376,355,331,384,347,fill='coral')
nextArrow.visible=False

def checkAnswer(clickedNumber):
    realAnswer=app.allAnswers[app.questionNumber]
    
    if clickedNumber == realAnswer:
        helpText.value="Excellent! That's Correct."
        helpText.fill='darkGreen'
        if app.wrongClicks == 0:
            app.totalRight +=1
            app.scoreHistory.append('Pass')
        else:
            app.scoreHistory.append('Fail')
        
        nextArrow.visible=True
    
    else:
        app.wrongClicks+=1
        if app.wrongClicks == 1:
            helpText.Value = "Not quite. Try one more Time!"
            helpText.Fill='crimson'
        else:
            helpText.value= "The correct answer was " + str(realAnswer)
            helpText.fill='darkOrange'
            app.scoreHistory.append('Fail')
            nextArrow.Visible=True

def goNext():
    app.questionNumber+=1
    app.wrongClicks=0
    
    if (app.questionNumber < len(app.allAnswers)):
        questionText.value='6 x ' + str(app.questionNumber + 1) + "="
        helpText.value='Look at the question then click on the right answer:'
        helpText.fill='darkslateGray'
        nextArrow.visible=False
        
        realAnswer=app.allAnswers[app.questionNumber]
        choices = [realAnswer,realAnswer + 6, realAnswer - 3 if realAnswer - 3 > 0  else realAnswer + 12]
        random.shuffle(choices)
        for i in range (3):
            app.buttonsList[i].children[1].value=choices[i]
    else:
        app.quizShapes.clear()
        nextArrow.visible=False
        app.background="black"
        
        finalScore=int((app.totalRight/len(app.allAnswers)*100))
        Label("Quiz Finished ",200,60,size=26,fill='coral',font='monospace',bold=True)
        Label('Your Score:' + str(finalScore)+'%',200,100,size=22,fill="Khaki")
        
        yPos=140
        for result in app.scoreHistory:
            if result =="Pass":
                Label('Question: CORRECT',200,yPos,fill='springGreen',size=14,font='monospace')
            else:
                Label('Question: WRONG',200,yPos,fill='lightCoral',size=14,font='monospace')
            yPos+=22
def onMousePress(mouseX,mouseY):
    for btn in app.buttonsList:
        if btn.contains(mouseX,mouseY)and nextArrow.visible==False:
            clickedNumber = int (btn.children[1].value)
            checkAnswer(clickedNumber)
    if  nextArrow.visible and nextArrow.contains(mouseX,mouseY):
        goNext()
