from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import organizer
from pathlib import Path

window = Tk()
window.title("---|FILE ORGANIZER|---")
window.geometry("420x420")
window.config(bg = "#000000",
              padx = 40,
              pady = 10)

source_path = StringVar(value = "")
destination_path = StringVar(value = "")

def open_source_dir():
    path = filedialog.askdirectory(initialdir = Path().home(), title = "OPEN YOUR SOURCE DIRECTORY")
    if path:
        source_path.set(path)
        print(f"Source path set to: {path}")

def open_destination_dir():
    path = filedialog.askdirectory(initialdir = Path().home(), title = "OPEN YOUR DESTINATION DIRECTORY")
    if path:
        destination_path.set(path)
        print(f"Destination path set to: {path}")

def start_organizing():
    if not destination_path.get() or not source_path.get():
        messagebox.showwarning(title = "WARNING!", message = "Please select both source and destination path to continue.")
        return
    if destination_path.get() == source_path.get():
        messagebox.showwarning(title = "WARNING", message = "Source and Destination cannot be in the same directory!")
        return
    organizer.organise_folder(source_path = Path(source_path.get()), destination_path = Path(destination_path.get()))
    messagebox.showinfo(title = "DONE", message = "Files organized successfully!")

title = Label(master = window,
      text = "WELCOME TO 'FILE ORGANIZER'",
      font = ("Consolas", 15, "bold"),
      fg = "#00FF00",
      bg = "#000000",
      bd = 20,
      relief = None
      )
title.grid(row = 0, column = 0, columnspan = 3)

sourcefolderbrowse = Button(master = window,
                            command = open_source_dir,
                            text = "BROWSE",
                            fg = "#000000",
                            activeforeground = "#00FF00",
                            bg = "#00FF00",
                            activebackground = "#000000",
                            width = 7
                            )
sourcefolderbrowse.grid(row = 1, column = 2, columnspan = 1)

Label(master = window,
      textvariable = source_path,
      width = 40
      ).grid(row = 1, column = 0, columnspan = 2)

destinationfolderbrowse = Button(master = window,
                            command = open_destination_dir,
                            text = "BROWSE",
                            fg = "#000000",
                            activeforeground = "#00FF00",
                            bg = "#00FF00",
                            activebackground = "#000000",
                            width = 7
                            )
destinationfolderbrowse.grid(row = 2, column = 2, columnspan = 1)

Label(master = window,
      textvariable = destination_path,
      width = 40
      ).grid(row = 2, column = 0, columnspan = 2)

start_organizing_button = Button(master = window,
                            command = start_organizing,
                            text = "ORGANIZE",
                            fg = "#000000",
                            bg = "#00FF00",
                            activebackground = "#000000",
                            activeforeground = "#00FF00",
                            width = 7
                            )
start_organizing_button.grid(row = 3, column = 0, columnspan = 3)

window.mainloop()