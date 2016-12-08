import RPi.GPIO as GPIO
import time
from Tkinter import *
from PIL import Image,ImageTk

#########//////First the GPIO setup/////##########

GPIO.setmode(GPIO.BOARD) # sets the GPIO mode

GPIO.setup(11,GPIO.OUT) # allows digital pin 11 to output information to servo so pulse with modulation can be used
GPIO.setup(18,GPIO.OUT) # allows digital pin 11 to output information to servo so pulse with modulation can be used

pwmTurn = GPIO.PWM(11,100) # PWM function allows us to access its functions
pwmDrive = GPIO.PWM(18,100) # same thing as ^

pwmTurn.start(0) # starts servo that turns the wheels @ 0
pwmDrive.start(0) # starts servo that drives back and forth @ 0


##########/////Second the GUI setup/////##########

main = Tk()
main.title("Rc Car Control")
main.geometry("300x300")


path = "arrows.png"

img = ImageTk.PhotoImage(Image.open(path))
panel = Label(main, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
text = Text(main)
text.insert(INSERT, "RC Robot Car Control with Raspberry Pi\nBy Noah Gaeta")
text.insert(END,"")
text.config(state=DISABLED)
#########/////Now time for Servo Control////########
driveNumber = 1


turnNumber = 1



def leftKey(event):
    print "Left key pressed"
    if turnNumber >= 50 and number <=100:
    	turnNumber = turnNumber + 1
    else:
    	turnNumber = 50
    pwmTurn.ChangeDutyCycle(turnNumber)




def rightKey(event):
    print "Right key pressed"
    if turnNumber >= 1 and number <=49:
    	turnNumber = turnNumber + 1
    else:
    	turnNumber = 1
    pwmTurn.ChangeDutyCycle(turnNumber)




def upKey(event):
	print "Up key pressed"
	if driveNumber >= 50 and driveNumber <=100:
		driveNumber = driveNumber + 1
	else:
		driveNumber = 50
	pwmTurn.ChangeDutyCycle(driveNumber)



def downKey(event):
	print "Down key pressed"
	if driveNumber >= 1 and driveNumber <=49:
		driveNumber = driveNumber + 1
	else:
		driveNumber = 1
	pwmTurn.ChangeDutyCycle(driveNumber)

###########////GUI Binding and packing + GPIO cleanup /////###########
frame = Frame(main, width=100, height=100)

frame.bind('<Left>', leftKey)

frame.bind('<Right>', rightKey)

frame.bind('<Up>',upKey)

frame.bind('<Down>',downKey)

text.bind('<Left>', leftKey)

text.bind('<Right>', rightKey)

text.bind('<Up>',upKey)

text.bind('<Down>',downKey)

frame.focus_set()

text.focus_set()

text.pack()

frame.pack()

main.mainloop()

GPIO.cleanup()


#####################################################
###########////////By Noah Gaeta/////////############
#####################################################
