import serial as sr
import tkinter as tk

def on1(): # fungsi saat tombol "on1" ditekan
    s.write(b',a') # mengirim karakter "a" ke arduino
def off1(): # fungsi saat tombol "off1" ditekan
    s.write(b',b') # mengirim karakter "b" ke arduino
def on2(): # fungsi saat tombol "on2" ditekan
    s.write(b',c') # mengirim karakter "a" ke arduino
def off2(): # fungsi saat tombol "off2" ditekan
    s.write(b',d') # mengirim karakter "b" ke arduino

#------Kode Utama GUI------
root = tk.Tk()
root.title('kontrol lampu')
root.configure(background = 'yellow')
root.geometry("250x150") #seting ukuran tampilan

#------Membuat Tombol 1------
root.update();
menyala = tk.Button(root,text = "Nyala", font = ('calibri',12), command = lambda: on1(), bg="magenta")
menyala.place(x = 50, y = 50 )

root.update();
padam = tk.Button(root, text = "Padam", font = ('calibri',12), command = lambda: off1(), bg="orange")
padam.place(x = menyala.winfo_x()+menyala.winfo_reqwidth() + 50, y = 50 )

#------Membuat Tombol 2------
root.update();
menyala = tk.Button(root,text = "Nyala", font = ('CALIBRI',12), command = lambda: on2(), bg="white")
menyala.place(x = 50, y = 100 )

root.update();
padam = tk.Button(root, text = "Padam", font = ('CALIBRI',12), command = lambda: off2(), bg="red")
padam.place(x = menyala.winfo_x()+menyala.winfo_reqwidth() + 50, y = 100 )

#------Memulai Setting Port Serial------
s = sr.Serial('COM21',9600);

root.mainloop()
