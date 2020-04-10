from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

output_size = (300, 300)

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
i = Image.open(file_path)
fn = os.path.split(file_path)[1]
save_path = "C:\\Users\\cweic\\Fotoalbum\\" + fn
#print(save_path)

i.thumbnail(output_size)
i.save(save_path)
