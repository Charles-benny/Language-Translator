import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from googletrans import Translator

def draw_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    
    (r1, g1, b1) = canvas.winfo_rgb(color1)
    (r2, g2, b2) = canvas.winfo_rgb(color2)
    
    r_ratio = float(r2 - r1) / height
    g_ratio = float(g2 - g1) / height
    b_ratio = float(b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))

        color = f'#{nr>>8:02x}{ng>>8:02x}{nb>>8:02x}'
        canvas.create_line(0, i, width, i, fill=color)

def on_resize(event):
    canvas = event.widget
    canvas.delete("all")
    draw_gradient(canvas, "#D8B5FF", "#FE8C8C")

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()
    
    if not lang_1.strip():
        messagebox.showerror("Error", "Please enter text to translate.")
        return
    else:
        text_entry2.delete(1.0, "end")
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert('end', output.text)

def clear():
    text_entry1.delete(1.0, "end")
    text_entry2.delete(1.0, "end")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_entry1.delete(1.0, "end")
            text_entry1.insert("end", content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            content = text_entry2.get(1.0, "end-1c")
            file.write(content)

def exit_app():
    root.quit()

def update_status(event):
    status_bar.config(text=f"Cursor Position: {event.x}, {event.y}")

root = tk.Tk()
root.title('Language Translator App')
root.geometry('650x500')
root.configure(bg='#1A1A1A')

frame1 = tk.Frame(root, width=650, height=600, relief=tk.RIDGE, borderwidth=5)
frame1.place(x=0, y=0)

menu_bar = tk.Menu(root, bg='#1A1A1A', fg='white')
file_menu = tk.Menu(menu_bar, tearoff=0, bg='#1A1A1A', fg='white')

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

canvas = tk.Canvas(frame1, width=640, height=590)
canvas.pack(expand=tk.YES, fill=tk.BOTH)
canvas.bind("<Configure>", on_resize)

tk.Label(root, text="Language Translator", font=("Helvetica", 25, "bold"), fg="Black", bg="#FFFFC7").pack(pady=10)

text_entry1 = tk.Text(frame1, width=22, height=7, borderwidth=4, relief=tk.RIDGE, font=('verdana', 15), bg='#111111', fg='white')
text_entry1.place(x=20, y=100)

text_entry2 = tk.Text(frame1, width=22, height=7, borderwidth=4, relief=tk.RIDGE, font=('verdana', 15), bg='#111111', fg='white')
text_entry2.place(x=330, y=100)

btn1 = tk.Button(frame1, text="Translate", relief=tk.RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#000000', fg='white', cursor='hand2', command=translate)
btn1.place(x=275, y=350)

btn2 = tk.Button(frame1, text="Clear", relief=tk.RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#000000', fg='white', cursor='hand2', command=clear)
btn2.place(x=289, y=390)

label = tk.Label(frame1, text="Mini Project by: Akash. J", borderwidth=1, font=('verdana', 9), fg='black', cursor='hand2')
label.place(x=45, y=450)

a = tk.StringVar()
auto_select = ttk.Combobox(frame1, width=27, textvariable=a, state="readonly", font=('verdana', 10, 'bold'))
auto_select['values'] = ('Auto Select',)
auto_select.place(x=15, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state="readonly", font=('verdana', 10, 'bold'))
choose_language['values'] = (
    'Auto Select', 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 
    'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Simplified)', 'Chinese (Traditional)', 
    'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French',
    'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 
    'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 
    'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 
    'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (Burmese)', 
    'Nepali', 'Norwegian', 'Odia (Oriya)', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 
    'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 
    'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 
    'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'
)
choose_language.place(x=305, y=60)
choose_language.current(0)

status_bar = tk.Label(root, text="Cursor Position: 0, 0", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.bind("<Motion>", update_status)

root.mainloop()
