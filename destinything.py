from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title('Destiny Perk Calculator')
root.iconbitmap('images/sb.ico')
root.configure(background="black")

frame = LabelFrame(root, text="Destiny Perk Calculator", padx=50, pady=50, labelanchor=N, background="darkgray")
frame.pack(padx=10, pady=10)

welcomeLabel = Label(frame, text="Enter Base Magazine. Press Button. Wow!", borderwidth=2, relief="groove", padx=5, pady=5, background="lightblue")
welcomeLabel.grid(row=0, column=0, columnspan=3, pady=5)

e = Entry(frame, width=35, borderwidth=5, justify="center")
e.grid(row=1, column=0, columnspan=3, padx=10, pady=20) 

answerLabel = Label(frame, text="")

def triple():
    global answerLabel
    answerLabel.grid_forget()
    try:
        mag = int(e.get())
        mag_extended = mag + (mag - 1)/2
        answerLabel = Label(frame, text="Triple Tap Magazine is Now " + str(int(mag_extended)), borderwidth=2, relief="solid", padx=5, pady=5, background="lightblue")
        answerLabel.grid(row=4, column=0, columnspan=3, pady=20)
    except ValueError:
        answerLabel = Label(frame, text="Please Enter an Integer", borderwidth=2, relief="solid", padx=5, pady=5, background="pink")
        answerLabel.grid(row=4, column=0, columnspan=3, pady=20)

def trip_dub():
    global answerLabel
    answerLabel.grid_forget()
    try:
        mag = int(e.get())
        mag_extended = 2 + ((mag - 2) * 3)
        answerLabel = Label(frame, text="Triple Double Magazine is Now " + str(int(mag_extended)), borderwidth=2, relief="solid", padx=5, pady=5, background="lightblue")
        answerLabel.grid(row=4, column=0, columnspan=3, pady=20)
    except ValueError:
        answerLabel = Label(frame, text="Please Enter an Integer", borderwidth=2, relief="solid", padx=5, pady=5, background="pink")
        answerLabel.grid(row=4, column=0, columnspan=3, pady=20)
        
def fourth_charm():
    global answerLabel
    answerLabel.grid_forget()
    try:
        mag = int(e.get())
        mag_extended = mag = (2 * mag) - (mag % 2) - 2
        answerLabel = Label(frame, text="Fourth Time's the Charm Magazine is Now " + str(int(mag_extended)), borderwidth=2, relief="solid", padx=5, pady=5, background="lightblue")
        answerLabel.grid(row=4, column=0, columnspan=3, pady=20)
    except ValueError:
        answerLabel = Label(frame, text="Please Enter an Integer", borderwidth=2, relief="solid", padx=5, pady=5, background="pink")
        answerLabel.grid(row=4, column=0, columnspan=3, pady=20)

tt_icon = PhotoImage(file=str("images/tt.png"))
td_icon = PhotoImage(file=str("images/td.png"))
fc_icon = PhotoImage(file=str("images/fc.png"))

b = Button(frame, image=tt_icon, text="Triple Tap", foreground="white", background="gray", command=triple, compound="top")
b2= Button(frame, image=td_icon, text="Triple Double", foreground="white", background="gray", command=trip_dub, compound="top")
b3= Button(frame, image=fc_icon, text="Fourth Time's the Charm", foreground="white", background="gray", command=fourth_charm, compound="top")

b.grid(row=2, column=0, padx=10) #Normally cant mix grids and packs, but frames can take grids
b2.grid(row=2, column=1, padx=10) #Normally cant mix grids and packs, but frames can take grids
b3.grid(row=2, column=2, padx=10) #Normally cant mix grids and packs, but frames can take grids

   

root.mainloop()