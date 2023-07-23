import tkinter as tk
from tkinter import messagebox

def show_info_message():
    messagebox.showinfo("Bilgi", "Bu bir bilgi mesajıdır.")

def show_warning_message():
    messagebox.showwarning("Uyarı", "Bu bir uyarı mesajıdır.")

def show_error_message():
    messagebox.showerror("Hata", "Bu bir hata mesajıdır.")

def ask_question():
    result = messagebox.askquestion("Soru", "Devam etmek istiyor musunuz?")
    if result == "yes":
        print("Kullanıcı devam etmek istiyor.")
    else:
        print("Kullanıcı devam etmek istemiyor.")

def ask_yes_no_cancel():
    result = messagebox.askyesnocancel("Soru", "Kaydetmek istiyor musunuz?")
    if result is True:   # Yes seçeneği seçildi
        print("Kullanıcı kaydetmek istiyor.")
    elif result is False:  # No seçeneği seçildi
        print("Kullanıcı kaydetmek istemiyor.")
    else:  # Cancel seçeneği seçildi
        print("Kullanıcı işlemi iptal etti.")

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Messagebox Örnek")

# Butonlar oluşturma
info_button = tk.Button(root, text="Bilgi Mesajı", command=show_info_message)
info_button.pack(pady=5)

warning_button = tk.Button(root, text="Uyarı Mesajı", command=show_warning_message)
warning_button.pack(pady=5)

error_button = tk.Button(root, text="Hata Mesajı", command=show_error_message)
error_button.pack(pady=5)

question_button = tk.Button(root, text="Soru Sor", command=ask_question)
question_button.pack(pady=5)

yes_no_cancel_button = tk.Button(root, text="Yes/No/Cancel Sor", command=ask_yes_no_cancel)
yes_no_cancel_button.pack(pady=5)

# Tkinter penceresini çalıştırma
root.mainloop()