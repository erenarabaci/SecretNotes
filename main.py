import tkinter
from tkinter import messagebox
### pencere ###
window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(400,800)
window.config(padx=40,pady=40)
FONT = ("arial",20,"normal")

### kayıt etme ###

def Save():
    with open("Notes.txt","a") as note :
        inputtitle = titleEntry.get()
        inputtext = txt.get("1.0",tkinter.END)
        masterkey = masterkeyEntry.get()

        if inputtext == "" or inputtitle == "" or masterkey == "":
            messagebox.showerror(message="Check Your Inputs",title="Error!!!")
        else:
            try:

                note.write(inputtitle + "\n")
                note.write(inputtext)
                print(txt.get("1.0", tkinter.END))

            except :
                pass

            finally:
                titleEntry.delete(0,tkinter.END)
                txt.delete("1.0",tkinter.END)
                masterkeyEntry.delete(0,tkinter.END)





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
saveButton.config(text="Save % Encrypt",width=20,command=Save)
saveButton.pack()

decryptButton = tkinter.Button()
decryptButton.config(text="Decrypt",width=10)
decryptButton.pack()


### kayıt etme ###














































window.mainloop()