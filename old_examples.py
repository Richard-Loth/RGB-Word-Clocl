import os, random
from tkinter import *

# root = Tk()
# app = ButtonApp(root)
#
# label = Label(root, fg="red")
# label.pack()
# app.counter_label(label)
#
# root.mainloop()

# Slider Example
# def show_values():
#     print(w1.get(), w2.get())
#
#
# master = Tk()
# w1 = Scale(master, from_=0, to=42)
# w1.pack()
# w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL, tickinterval=10, length=500)
# w2.pack()
#
# b = Button(master, text='show', command=show_values).pack()
#
# master.mainloop()

# Easy grid example
# colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']
# r = 0
# for c in colours:
#     Label(text=c, relief=RIDGE, width=15).grid(row=r, column=0)
#     Entry(bg=c, relief=SUNKEN, width=10).grid(row=r, column=1)
#     r = r + 1
#
# mainloop()

listRow1 = [5, 9, 3, 1, 3]
listRow1.append(45)
listRow2 = []
listRow2.append(random.randrange(48))
listRow2.append(random.randrange(48))
listRow2.append(random.randrange(48))
listRow2.append(random.randrange(48))
listRow2.append(random.randrange(48))

listOfLists = [listRow1, listRow2]

for singleList in listOfLists:
    for number in singleList:
        print(str(number) + ', ', end='')
    print(os.linesep)

# class Application(Frame):
#     def say_hi(self):
#         print ("hi there, everyone!")
#
#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT"
#         self.QUIT["fg"]   = "red"
#         self.QUIT["command"] =  self.quit
#
#         self.QUIT.pack({"side": "left"})
#
#         self.hi_there = Button(self)
#         self.hi_there["text"] = "Hello",
#         self.hi_there["command"] = self.say_hi
#
#         self.hi_there.pack({"side": "left"})
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#
# root = Tk()
#
#
# app = Application(master=root)
# app.mainloop()
# root.destroy()



counter = 0

class ButtonApp:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="OK", fg="orange", command=frame.quit)
        self.button.pack(side=LEFT)

    def counter_label(self, label):
        counter = 0

        def count():
            global counter
            counter += 1
            label.config(text=str(counter))
            label.after(1000, count)

        count()

        # photo = PhotoImage(file="resources/tails.gif")
        # photoLabel = Label(root, image=photo)
        # photoLabel.image = photo  # keep a reference!