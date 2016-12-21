from Tkinter import *
import time
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

##for x in range(0,60):
##    canvas.move(1,5,0)
##    tk.update()
##    time.sleep(0.05)

def movetriangle(event):
    canvas.move(1,5,0)
canvas.bind_all('<KeyPress-Return>',movetriangle)


##my_image=PhotoImage(file="53D.gif")
##canvas.create_image(0,0, anchor=NW, image=my_image)

tk.mainloop()

