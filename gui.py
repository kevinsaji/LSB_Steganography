import tkinter as tk
from tkinter import filedialog


def e_d_func():
    return var.get()


def text_func():
    return var1.get()


def close_window(root):
    root.destroy()


height = 500
width = 800
root = tk.Tk()

var = tk.IntVar()
var1 = tk.StringVar()
canvas = tk.Canvas(root, height=height, width=width, bg='#EFC9AF')
canvas.pack()

frame1 = tk.Frame(canvas, bg='#F0BB97')
frame1.place(relwidth=1, relheight=0.333, rely=0)

frame2 = tk.Frame(canvas, bg='#E0A379')
frame2.place(relwidth=1, relheight=0.333, rely=0.333)

exit_button = tk.Button(frame1, text='SUBMIT', command=lambda: close_window(root))
exit_button.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.4, relheight=0.2)

head_label = tk.Label(frame1, text='STEGANOGRAPHY PROJECT', bg='#F0BB97', font=('Helvetica', 20))
head_label.place(anchor='n', relx=0.5, rely=0.5, relwidth=0.6, relheight=0.2)

e_d_label = tk.Label(frame2, text='SELECT YOUR OPTION', bg='#E0A379', font=('Helvetica', 20))
e_d_label.place(anchor='n', relx=0.5, rely=0.175, relwidth=0.4, relheight=0.2)

e_rad_button = tk.Radiobutton(frame2, text='Encode', variable=var, value=1, command=e_d_func, bg='#E0A379',
                              font=('Helvetica', 20))
e_rad_button.place(anchor='n', relx=0.25, rely=0.45, relwidth=0.4, relheight=0.2)

d_rad_button = tk.Radiobutton(frame2, text='Decode', variable=var, value=2, command=e_d_func, bg='#E0A379',
                              font=('Helvetica', 20))
d_rad_button.place(anchor='n', relx=0.75, rely=0.45, relwidth=0.4, relheight=0.2)

enter_text_label = tk.Label(canvas, text='Enter Text(IF ENCODING)', bg='#EFC9AF', font=('Helvetica', 20))
enter_text_label.place(anchor='n', relx=0.5, rely=0.67, relwidth=0.7, relheight=0.1)

root.update_idletasks()  # This is a test to fix the focus issue.
text_box = tk.Entry(canvas, textvariable=var1)
text_box.place(anchor='n', relx=0.5, rely=0.785, relwidth=0.7, relheight=0.075)

root.filename = filedialog.askopenfilename(title="Select the file")

root.mainloop()
