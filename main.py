import customtkinter as ctk

fonte_t = ("Inter", 36, 'bold')
fonte = ("Inter", 20, 'bold')
fonte_terminal = ("Inter", 12)
common_pady = 20

wn = ctk.CTk()
wn.geometry('360x800')
wn.config(background='white')
wn.resizable(False, False)
wn.title('EmailReader')

titulo = ctk.CTkLabel(wn, text='EmailReader', font=fonte_t, fg_color='white', text_color='black')
titulo.pack(pady=common_pady)

fm = ctk.CTkFrame(wn, fg_color='#F2F2F2', corner_radius=0, height=650)
fm.pack_propagate(False)
fm.pack(expand=True, fill='x')

email_entry = ctk.CTkEntry(fm, placeholder_text='Email', justify='center', width=300, height=60, font=fonte, text_color='black', fg_color='white', corner_radius=45, border_color='white', placeholder_text_color='black')
email_entry.pack(pady=common_pady)

password_entry = ctk.CTkEntry(fm, placeholder_text='Senha', justify='center', width=300, height=60, font=fonte, text_color='black', fg_color='white', corner_radius=45, border_color='white', placeholder_text_color='black')
password_entry.pack(pady=common_pady)

chave_entry = ctk.CTkEntry(fm, placeholder_text='Título-chave', justify='center', width=300, height=60, font=fonte, text_color='black', fg_color='white', corner_radius=45, border_color='white', placeholder_text_color='black')
chave_entry.pack(pady=common_pady)

fetch_button = ctk.CTkButton(fm, fg_color='#A9D18E', text='Fetch', font=fonte, hover_color='#000000', text_color='white', corner_radius=45, width=240, height=50)
fetch_button.pack(pady=common_pady)

terminal_box = ctk.CTkTextbox(fm, fg_color='white', font=fonte_terminal, text_color='black', height=120)
terminal_box.pack(pady=common_pady, expand=True, fill="x")

joindf_button = ctk.CTkButton(fm, fg_color='#A9D18E', text='Juntar DataFrames', font=fonte, hover_color='#000000', text_color='white', corner_radius=45, width=240, height=50)
joindf_button.pack(pady=common_pady)

wn.mainloop()
