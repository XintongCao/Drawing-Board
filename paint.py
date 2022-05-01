from tkinter import *
# define an object of tkinter
drawing=Tk()
# set two frames for drawing board. One is for actual painting, the other one is for the function options
frame1=Frame(drawing)
frame1.pack(padx=50,pady=50,side=LEFT)
frame2=Frame(drawing)
frame2.pack(padx=50,pady=50,side=RIGHT)
# define a title for this app
drawing.title('<Drawing Board>')

# for <frame 1>
# set a label to expain how to use this app
Label(frame1,text='Hold down the left mouse button and drag slowly. Start drawing your first picture!😊')\
      .grid(row=0,padx=30,pady=30)
# define a canvas
painting=Canvas(frame1,width=600,height=700,background='white')
painting.grid(padx=40)
# define a function to draw circles
def paint(event):
    # define two sets of X and Y axes
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    # set a circle
    global points
    points=painting.create_oval(x1,y1,x2,y2,outline=f'{color_selection()}',fill=f'{color_selection()}')
    return points
# binding the left mouse button to the drawing function
painting.bind('<B1-Motion>',paint)

# for <frame 2>
# define a label for function panel
Label(frame2,text='<Function Panel>').grid(row=0,column=0,sticky=N)
#改变颜色的功能爱需要进一步的完善和更新，目前还不可用
# set labels to explain different buttons for different functions
Label(frame2,text='(1)Press the buttons to change the color of the drawing lines: ').grid(row=1,column=0)
# set the color change options
#color_change=[('red',1),('yellow',2),('blue',3),('green',4),('pink',5),('purple',6),('black',7)]
var_color=IntVar()
# define a function to show the outputs of the Radiobutton, e.g., changed color
def color_selection():
    color=var_color.get()
    if color==1:
        output='red'
    elif color==2:
        output='yellow'
    elif color==3:
        output='blue'
    elif color==4:
        output='green'
    elif color==5:
        output='pink'
    elif color==6:
        output='purple'
    elif color==7:
        output='black'
    return output
Radiobutton(frame2,text='red',variable=var_color,value=1,command=color_selection).grid(row=1,column=1)
Radiobutton(frame2,text='yellow',variable=var_color,value=2,command=color_selection).grid(row=2,column=1)
Radiobutton(frame2,text='blue',variable=var_color,value=3,command=color_selection).grid(row=3,column=1)
Radiobutton(frame2,text='green',variable=var_color,value=4,command=color_selection).grid(row=4,column=1)
Radiobutton(frame2,text='pink',variable=var_color,value=5,command=color_selection).grid(row=5,column=1)
Radiobutton(frame2,text='purple',variable=var_color,value=6,command=color_selection).grid(row=6,column=1)
Radiobutton(frame2,text='black',variable=var_color,value=7,command=color_selection).grid(row=7,column=1)
var_color.set(7)

# set a label to explain 'Delete' function
Label(frame2,text='(2)If you want to draw a new picture, please press the <DELETE ALL> button: ').grid(row=8,column=0)
def dele():
    painting.delete(ALL)
Button(frame2,text='DELETE ALL',command=dele).grid(row=8,column=1)
# set the button to exit
Label(frame2,text='(3)Press the <EXIT> button to leave this APP: ').grid(row=9,column=0)
Button(frame2,text='EXIT',command=frame2.quit).grid(row=9,column=1)
mainloop()
