import tkinter
from tkinter import messagebox
import base64
### pencere ###
window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(400,800)
window.config(padx=40,pady=40)
FONT = ("arial",20,"normal")

### kayıt etme ###

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def Save():
    with open("Notes.txt","a") as note :
        inputtitle = titleEntry.get()
        inputtext = txt.get("1.0",tkinter.END)
        masterkey = masterkeyEntry.get()

        if inputtext == "" or inputtitle == "" or masterkey == "":
            messagebox.showerror(message="Check Your Inputs",title="Error!!!")
        else:

            encryptedmessage = encode(masterkey,inputtext)
            try:

                note.write(inputtitle + "\n")
                note.write(encryptedmessage+"\n")
                print(txt.get("1.0", tkinter.END))

            except :
                pass

            finally:
                titleEntry.delete(0,tkinter.END)
                txt.delete("1.0",tkinter.END)
                masterkeyEntry.delete(0,tkinter.END)


def decryptnote():
    messageecrypted = txt.get("1.0",tkinter.END)
    masterkey = masterkeyEntry.get()


    if messageecrypted == "" or masterkey == "":
        messagebox.showerror(title="Error!!!",message="Check Your Inputs")
    else :
        decryptedmessage = decode(masterkey,messageecrypted)
        txt.delete("1.0", tkinter.END)
        txt.insert("1.0",decryptedmessage)






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
decryptButton.config(text="Decrypt",width=10,command=decryptnote)
decryptButton.pack()


### kayıt etme ###














































window.mainloop()