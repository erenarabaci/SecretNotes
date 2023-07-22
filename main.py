import tkinter
### pencere ###
window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(400,800)
window.config(padx=40,pady=40)
FONT = ("arial",20,"normal")
#### UI ####
image = tkinter.PhotoImage(file="resim.png")
imagelabel =tkinter.Label(window , image=image)
imagelabel.config(width=200,height=200)
imagelabel.pack()

titlelabel = tkinter.Label(text="Enter Your Title ")
titlelabel.pack()
titleEntry = tkinter.Entry(width=30)
titleEntry.pack()

textlabel = tkinter.Label(text="Enter Your Secret Note")
textlabel.pack()
txt = tkinter.Text()
txt.config(width=40,height=20)
txt.pack()

masterkeylabel = tkinter.Label(text="Enter Your Master Key")
masterkeylabel.pack()

masterkeyEntry = tkinter.Entry()
masterkeyEntry.config(width=30)
masterkeyEntry.pack()

saveButton = tkinter.Button()
saveButton.config(text="Save % Encrypt",width=20)
saveButton.pack()

decryptButton = tkinter.Button()
decryptButton.config(text="Decrypt",width=10)
decryptButton.pack()













































window.mainloop()