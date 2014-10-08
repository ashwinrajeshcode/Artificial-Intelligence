#
# Jake Shankman, October 18th, 2011
#
# Sliding Tile Puzzles: Lab06
#
#   Input: none
# Process: A sliding tile puzzle appears
#  Output: Graphical display of puzzle, tiles out of place and moves left until the puzzle is solved
#

from Tkinter import *
from sys import exit

w,h=800,600
x,y,dx,dy=100,50,175,175
xspace = 1
yspace = 1
alist = []
finalist= ['1', '2', '3', '4', '5', '6', '7', '8', '']
k=0
while k <= 8:
  if k == 8:
    alist.append('')
  else:
    alist.append(str(k+1))
  k = k+1
print len(alist)
print alist

def outOfPlace():
   k = 0
   outP = 0
   while k <= 8:
    if k == 8:
      if alist[k] != '':
	outP = outP + 1
    else: 
     if alist[k] != str(k +1):
       outP = outP + 1
    k = k +1
   return outP

def manhattan():
   k = 0
   distance = 0
   while k < 9:
    if finalist[k] == '':
      distance = distance
    else:
      dex = alist.index(finalist[k])
      kr = k/3
      kc = k%3
      dexr = dex/3
      dexc = dex%3
      distance = distance + abs(dexr - kr) + abs(dexc - kc)
    k = k +1
   return distance

     

def tick():
#	x1,y1,x2,y2=canvas.coords(rect)
#	print x1,y1,x2,y2
	#canvas.coords(rect,x,y,x+dx,y+dy) # move the objects
	canvas.after(10,tick) # animation

def click(evnt):
	r = (evnt.y - y)/dy
	ru = r - 1
	rd = r + 1
	c = (evnt.x - x)/dx
	cl = c - 1
	cr = c + 1
	if r > 2 or r < 0 or c >2 or c < 0:
	  print 'out of bounds'
	  return
	index =  c + (r)*3
	print index, 'i'
	if cl >= 0:
	  indexl = c - 1 + (r)* 3
	  print indexl, 'l'
	else:
	  indexl = -1
	if cr < 3:
	  indexr = c + (r - 1)*3 + 4
	  print indexr, 'r'
	else:
	  indexr = -1
	if ru >= 0:
	  indexu = c + (r - 1)*3
	  print indexu, 'u'
	else:
	  indexu = -1
	if rd < 3:
	  indexd = c + (r + 1)*3
	  print indexd, 'd'
	else:
	  indexd = -1
	#
	#INDEX R
	#
	if alist[indexr] == '' and indexr != -1:
	  temp = alist[index]
	  alist[index] = alist[indexr]
	  alist[indexr] = temp
	  canvas.itemconfigure(textlist[indexr], text = alist[indexr])
	  canvas.itemconfigure(textlist[index], text = alist[index])
	#
	##INDEX U
	##
	if alist[indexu] == '' and indexu != -1:
	  temp = alist[index]
	  alist[index] = alist[indexu]
	  alist[indexu] = temp
	  canvas.itemconfigure(textlist[indexu], text = alist[indexu])
	  canvas.itemconfigure(textlist[index], text = alist[index])
	#INDEX D
	if alist[indexd] == '' and indexd != -1:
	  temp = alist[index]
	  alist[index] = alist[indexd]
	  alist[indexd] = temp
	  canvas.itemconfigure(textlist[indexd], text = alist[indexd])
	  canvas.itemconfigure(textlist[index], text = alist[index])
	#INDEX L
	if alist[indexl] == '' and indexl != -1:
	  temp = alist[index]
	  alist[index] = alist[indexl]
	  alist[indexl] = temp
	  canvas.itemconfigure(textlist[indexl], text = alist[indexl])
	  canvas.itemconfigure(textlist[index], text = alist[index])
	hue1 = outOfPlace()
	canvas.itemconfigure(hueristic1, text = str(hue1))
	canvas.itemconfigure(hueristic2, text = str(manhattan()))

def quit(evnt):
	exit(0)

#
# Initialize.
#
root=Tk()
canvas=Canvas(root,width=w,height=h,bg='white')
canvas.pack()
#
# Graphics objects. 

#
rlist = []
textlist = []
row = 0
column = 0
while row < 3:
  while column <3: 
    rect=canvas.create_rectangle(x +column * dx + xspace, yspace +y + row * dy,x + (column +1) * dx,y+(row + 1)*dy,fill='gray',outline='white')
    rlist.append(rect)
    number = str(alist.pop(0))
    if number == '9':
      number = ''
    text=canvas.create_text((2*x +(2*column +1) * dx + xspace)/2, (yspace +2*y + (2*row + 1)* dy)/2,text=number,fill='white', font = 'Courier 48')
    textlist.append(text)
    column = column + 1
  column = 0
  row = row + 1
#make hueristic
hueristic1 = canvas.create_text(700, 150,text='0',fill='gray', font = 'Courier 48')
hueristic2 = canvas.create_text(700, 300,text='0',fill='gray', font = 'Courier 48')
#hueristic3 = canvas.create_text(700, 450,text='0',fill='gray', font = 'Courier 48')
#remake alist
k=0
while k <= 8:
  if k == 8:
    alist.append('')
  else:
    alist.append(str(k+1))
  k = k+1
#3 sets of copy variables to manipulate with three loops and counter to keep track of original textplacement
#swap method
#
# Callbacks.
#
root.bind('<Button-1>',click)
root.bind('<q>',quit)
canvas.after(10,tick) # animation
#
# Here we go.
#
root.mainloop()