import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(title="Select TACTICS.CFG", filetypes=[("CFG files", "*.CFG")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def update_name():
    file_path = file_entry.get()
    new_name = name_entry.get()
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                if "PlayerName =" in line:
                    line = f"PlayerName ={new_name}\n"
                file.write(line)
        status_label.config(text="Player name updated successfully!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

def add_character(char):
    current_text = name_entry.get()
    name_entry.delete(0, tk.END)
    name_entry.insert(0, current_text + char)

root = tk.Tk()
root.title("DarkReignAsciiNameGenerator2")

file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_label = tk.Label(file_frame, text="TACTICS.CFG Path:")
file_label.pack(side=tk.LEFT)

file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT)

file_button = tk.Button(file_frame, text="Browse", command=select_file)
file_button.pack(side=tk.LEFT)

name_frame = tk.Frame(root)
name_frame.pack(pady=10)

name_label = tk.Label(name_frame, text="New Player Name:")
name_label.pack(side=tk.LEFT)

name_entry = tk.Entry(name_frame, width=50)
name_entry.pack(side=tk.LEFT)

ascii_frame = tk.Frame(root)
ascii_frame.pack(pady=10)

# Extended ASCII characters for the buttons
ascii_chars = [
    "À", "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï",
    "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à",
    "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð",
    "ñ", "ò", "ó", "ô", "õ", "ö", "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ", "ƒ", "€",
    "©", "®", "™", "±", "¶", "§", "µ", "¸", "¼", "½", "¾", "¿", "¡", "¢", "£", "¤",
    "¥", "¦", "¨", "«", "¬", "­", "®", "¯", "°", "±", "²", "³", "´", "µ", "¶", "·",
    "¸", "¹", "º", "»", "¼", "½", "¾", "¿", "À", "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç",
    "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×",
    "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", "á", "â", "ã", "ä", "å", "æ", "ç",
    "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷",
    "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ", "Œ", "œ", "Š", "š", "Ÿ"
]

# Create buttons in a grid layout
for i, char in enumerate(ascii_chars):
    btn = tk.Button(ascii_frame, text=char, command=lambda c=char: add_character(c), width=3)
    btn.grid(row=i // 10, column=i % 10, padx=2, pady=2)

update_button = tk.Button(root, text="Update Name", command=update_name)
update_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
