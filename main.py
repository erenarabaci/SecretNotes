import tkinter

window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(400,800)


image = tkinter.PhotoImage(file="resim.png")
imagelabel =tkinter.Label(window , image=image)
imagelabel.config(width=200,height=200)
imagelabel.pack()














































window.mainloop()