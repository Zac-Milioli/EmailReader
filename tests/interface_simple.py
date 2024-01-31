import tkinter as tk

fonte_t = ("Inter", 30)
fonte = ("Inter", 14)

wn = tk.Tk()
wn.geometry('360x800')
wn.configure(background='white')
wn.title('EmailReader')
wn.resizable(False, False)

titulo = tk.Label(wn, text='EmailReader', font=fonte_t, bg='white')
titulo.pack(pady=30)

fm = tk.Frame(wn, bg='#F2F2F2', height=650)
fm.grid_propagate(False)
fm.pack_propagate(False)
fm.pack(expand=True, fill='x')

email_entry = tk.Entry(fm, width=25, bg='white', font=fonte, fg='black')
email_entry.pack(pady=25, ipady=10)
senha_entry = tk.Entry(fm, width=25, bg='white', font=fonte, fg='black')
senha_entry.pack(pady=25, ipady=10)
chave_entry = tk.Entry(fm, width=25, bg='white', font=fonte, fg='black')
chave_entry.pack(pady=25, ipady=10)

botao1 = tk.Button(fm, text='Fetch', font=fonte, bg='#A9D18E', fg='white', width=15)
botao1.pack(pady=25)

terminal = tk.Entry(fm, width=25, bg='white', font=fonte, fg='black')
terminal.pack(pady=25, ipady=40)

botao2 = tk.Button(fm, text='Juntar DataFrames', fg='white', font=fonte, bg='#A9D18E', width=20, height=5)
botao2.pack(pady=25)

wn.mainloop()