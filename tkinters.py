#Libraries for using tkinter 
from tkinter import *
from tkinter import ttk

#these two make the text not blurry 
from ctypes import windll
from turtle import bgcolor 
windll.shcore.SetProcessDpiAwareness(1)  
#main tk part
root = Tk()
root.title('Tkinter Window Demo') 
message = Label(root, text="What is love?")
b=Button(root, text="Quit", command=root.destroy)
b.pack()
#Window adjustment
window_width = 800
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
message.pack()


# Canvas object/Circle
c= Canvas(root,width=300, height=300,)
c.pack()
c.create_oval(60,60,210,210, fill="red", outline="purple", width=5)

#Box 1
box1 = Label(root, text="This box is green but this text is blue", bg="green", fg="blue")
box1.pack(ipadx=20, ipady=20,)


root.mainloop()