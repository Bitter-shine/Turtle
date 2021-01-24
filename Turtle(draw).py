from turtle import *
color('yellow','green')
draw = begin_fill()
stop = end_fill()
draw
def draw():
   long = input("The long of the line:")
   forward(long)
   print("The 1 is left,The 2 is right.")
   du = input("Your du:")
   num = input("Your long:")
   if du == 1:
      left(num)
   elif du == 2:
      right(num)
   else:
      print("Number error,try agin!")
      draw()
while True:
   draw()      


