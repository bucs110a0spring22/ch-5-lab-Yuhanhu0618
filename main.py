import turtle
import random

#########################################################
#                   Your Code Goes Below                #
#########################################################
# Part A
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.up()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.down()
  for i in range (4):
    myturtle.forward(width)
    myturtle.right(90)
  myturtle.up()

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.goto(x_start, y_start)
  myturtle.down()
  myturtle.goto(x_end,y_end)
  myturtle.up()

def drawCircle(myturtle=None, radius=0, step=None):
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.circle(radius, 360, step)
  myturtle.up()

def setUpDartboard(myscreen=None, myturtle=None): 
  myturtle.color("black")
  turtle.setworldcoordinates(-2.5, -2.5, 2.5, 2.5)
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle=myturtle, x_start=-1.25, x_end=1.25)
  drawLine(myturtle=myturtle, y_start=1.25, y_end=-1.25)
  drawCircle(myturtle, 1, 100)

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  if myturtle.distance(0,0)<=1:
    return True
  return isInCircle

def throwDart(myturtle=None):  
  myturtle.goto(random.uniform(-1, 1), random.uniform(-1,1))
  myturtle.down()
  if isInCircle(myturtle, 0, 0, 1)==True:
    myturtle.color("green")
    myturtle.dot(3,"green")
    myturtle.up()
  else:
    myturtle.color("red")
    myturtle.dot(3,"red")
    myturtle.up()

def playDarts(myturtle=None):
  aPoints = 0
  bPoints = 0
  for i in range(10):
    throwDart(myturtle)
    if myturtle.color()[0]=="green":
      aPoints += 1  
    throwDart(myturtle)  
    if myturtle.color()[0]=="green":
      bPoints += 1
  print("Player A, your final score is:", aPoints,"Player B, your final score is:", bPoints)
  if aPoints > bPoints:
    print("Congrats player A! You win!")
  elif aPoints < bPoints:
    print("Congrats player B! You win")
  else:
    print("It's a tie.")
  
# Part C
def montePi(myturtle=None, num_darts=0):
  insideCount = 0
  for i in range(num_darts):
    throwDart(myturtle)
    if myturtle.color()[0]=="green":
      insideCount += 1
  approximatePi=insideCount/num_darts*4 
  return approximatePi
    
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()
main()
