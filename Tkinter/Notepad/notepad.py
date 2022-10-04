# Notepad app

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar

#Define window
root = tk.Tk()
root.title('Notepad')
root.iconbitmap('notepad.ico')
root.geometry('600x600')
root.resizable(0,0)

#Define fonts and colors
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"
root.config(bg=root_color)

#Define functions


#Define layout

#Define frames
menu_frame = tk.Frame(root, bg=menu_color)
text_frame = tk.Frame(root, bg=text_color)
menu_frame.pack(padx=5,pady=5)
text_frame.pack(padx=5,pady=5)

#Layout for menu frame
#Create the menu: new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open("new.png")) # make image
new_button = tk.Button(menu_frame, image=new_image) # put image on button
new_button.grid(row=0, column=0, padx=5, pady=5) # put button on the screen

open_image = ImageTk.PhotoImage(Image.open("open.png")) # make image
open_button = tk.Button(menu_frame, image=open_image) # put image on button
open_button.grid(row=0, column=1, padx=5, pady=5) # put button on the screen
 
save_image = ImageTk.PhotoImage(Image.open("save.png")) # make image
save_button = tk.Button(menu_frame, image=save_image) # put image on button
save_button.grid(row=0, column=2, padx=5, pady=5) # put button on the screen

close_image = ImageTk.PhotoImage(Image.open("close.png")) # make image
close_button = tk.Button(menu_frame, image=close_image, command=root.destroy  ) # put image on button
close_button.grid(row=0, column=3, padx=5, pady=5) # put button on the screen

#Create a list of fonts to use
families = ['Arial', 'Terminal', 'Elephant', 'Times New Roman Baltic', 'SimSun', 'Nirmala UI', '8514oem', 'Fixedsys', 'Bauhaus 93', 'Agency FB']

#Run the root window's main loop
root.mainloop()