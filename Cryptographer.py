from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from base64 import b64encode, b64decode
from itertools import cycle
import webbrowser
import os

class Cryptographer:
    def encrypt(self, key, data):
        cryptographed = self.xor(key, data)
        
        return b64encode(cryptographed.encode()).decode()
    
    def decrypt(self, key, data):
        try:
            data = b64decode(data.encode()).decode()
            cryptographed = self.xor(key, data)
            
            return cryptographed
            
        except:
            messagebox.showerror('ERROR', 'Please enter a valid encrypted text')
            
    @staticmethod
    def xor(key, text):
        result = ''
        for k, t in zip(cycle(key), text):
            result += ''.join(chr(ord(k) ^ ord(t)))
            
        return result


class Tab:
    def __init__(self, notebook, title, decrypt=False):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=title, padding=4)
        cryptographer = Cryptographer()
        personalize = {
            'selectbackground': 'blue', 'font': 'TkFixedFont', 'width': 20
            }
        
        self.keyVar = StringVar()
        Label(frame, text='Key: ').place(x=22, y=20)
        Entry(frame, textvariable=self.keyVar, **personalize).place(x=55, y=22)
        
        Label(frame, text='Text: ').place(x=20, y=60)
        self.text = Text(frame, height=5, **personalize)
        self.text.place(x=55, y=62)
        
        btn = Button(frame, text=title, width=22)
        btn.place(x=55, y=160)

        if decrypt:
            btn['command'] = lambda: self.insert_output(cryptographer.decrypt(self.keyVar.get(), self.text.get('1.0', 'end')))
        
        else:
            btn['command'] = lambda: self.insert_output(cryptographer.encrypt(self.keyVar.get(), self.text.get('1.0', 'end')))
        
        Label(frame, text='Output: ').place(x=5, y=200)
        self.output = Text(frame, height=5, **personalize)
        self.output.place(x=55, y=201)
        
    def insert_output(self, text):
        if self.keyVar.get():
            
            if self.text.get('1.0', 'end').strip():
                self.output.delete('1.0', 'end')
                self.output.insert('1.0', text)
                
            else:
                messagebox.showwarning('ERROR', 'Please enter a text!')
            
        else:
            messagebox.showwarning('ERROR', 'Please enter a key!')
        
    def clear(self):
        self.keyVar.set('')
        self.text.delete('1.0', 'end')
        self.output.delete('1.0', 'end')


class App:
    def __init__(self, master):
        master.config(menu=self.init_menu(master))
        master.bind('<Escape>', lambda _: self.clear())
                
        notebook = ttk.Notebook(master)
        notebook.place(relx=0.02, rely=0.02, relheight=.97, relwidth=0.97)
        
        self.encryptTab = Tab(notebook, '  Encrypt  ')
        self.decryptTab = Tab(notebook, '  Decrypt  ', decrypt=True)
    
    def clear(self):
        self.encryptTab.clear()
        self.decryptTab.clear()
        
    def show_about(self):
        dialog = Tk()
        dialog.title('About us')
        dialog.geometry('300x100+550+350')
        dialog.resizable(False, False)
        if os.path.exists(icon):
            dialog.iconbitmap(icon)
        dialog.focus_force()
        
        print('\a')
        Label(dialog, text='This program made by Sina.f').pack(pady=12)
        
        Button(dialog, text='GitHub', width=8, command=lambda: webbrowser.open('https://github.com/sina-programer')).place(x=30, y=50)
        Button(dialog, text='Instagram', width=8, command=lambda: webbrowser.open('https://www.instagram.com/sina.programer')).place(x=120, y=50)
        Button(dialog, text='Telegram', width=8, command=lambda: webbrowser.open('https://t.me/sina_programer')).place(x=210, y=50)
        
        dialog.mainloop()
        
    def init_menu(self, master):
        menu = Menu(master)
        menu.add_command(label='Clear', command=self.clear)
        menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', help_msg))
        menu.add_command(label='About us', command=self.show_about)
        
        return menu
    
        
help_msg = ''' You can encrypt and decrypt your texts with your own keys!\n
Steps:
1_ Enter a key
2_ Enter a text and click encrypt/decrypt button'''

icon = r'files\icon.ico'

if __name__ == "__main__":
    root = Tk()
    root.title('Cryptographer')
    root.resizable(False, False)
    root.geometry('270x350+550+230')
    
    if os.path.exists(icon):
        root.geometry('270x370+550+230')
        root.iconbitmap(icon)
    
    app = App(root)
    
    root.mainloop()
