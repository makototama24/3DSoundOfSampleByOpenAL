import tkinter as tk
import main
from PIL import Image, ImageTk
import tkinter.font as tkFont
from util import *


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.root.geometry(WINDOW_INITSIZE)
        COORDINATE_FONT = tkFont.Font(size=COORDINATE_FONTSIZE)
        BUTTON_FONT = tkFont.Font(size=BUTTON_FONTSIZE)
        self.audioSource = main.AudioSource()

        self.x_label = tk.Label(self.root, text='  x :', font=COORDINATE_FONT)
        self.y_label = tk.Label(self.root, text='  y :', font=COORDINATE_FONT)
        self.z_label = tk.Label(self.root, text='  z :', font=COORDINATE_FONT)

        self.x_entry = tk.Entry(self.root, width=ENTRY_SIZE)
        self.y_entry = tk.Entry(self.root, width=ENTRY_SIZE)
        self.z_entry = tk.Entry(self.root, width=ENTRY_SIZE)
        self.x_entry.insert(tk.END, ENTRY_INIT_x)
        self.y_entry.insert(tk.END, ENTRY_INIT_y)
        self.z_entry.insert(tk.END, ENTRY_INIT_z)

        self.play_button = tk.Button(
            self.root, text='再生', bg="skyblue", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT
            , command=lambda: self.audioSource.play(self.get_Coordinate()))
        self.xz_rotate_button = tk.Button(
            self.root, text='xz平面で回転', bg="pink", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT
            , command=lambda: self.audioSource.xz_rotate())

        self.image = Image.open(FIGURE)
        self.img = ImageTk.PhotoImage(self.image)
        self.canvas = tk.Canvas(bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

    def set_widget(self):
        self.x_label.grid(row=0, column=1)
        self.y_label.grid(row=1, column=1)
        self.z_label.grid(row=2, column=1)
        self.x_entry.grid(row=0, column=2, ipadx=ENTRY_ipadx, ipady=ENTRY_ipady, padx=ENTRY_padx)
        self.y_entry.grid(row=1, column=2, ipadx=ENTRY_ipadx, ipady=ENTRY_ipady, padx=ENTRY_padx)
        self.z_entry.grid(row=2, column=2, ipadx=ENTRY_ipadx, ipady=ENTRY_ipady, padx=ENTRY_padx)
        self.play_button.grid(row=3, column=1, columnspan=2)
        self.xz_rotate_button.grid(row=4, column=1, columnspan=2)
        self.canvas.grid(row=0, column=4, rowspan=4, columnspan=2)

    def main_loop(self):
        self.root.mainloop()

    def get_Coordinate(self):
        return self.x_entry.get(), self.y_entry.get(), self.z_entry.get()
