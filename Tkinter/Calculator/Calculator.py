# Simple Calculator App
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

#Define window 
root = tkinter.Tk()
root.title('Calculator')
root.iconbitmap('calc.ico')
root.geometry('300x400')
root.resizable(0,0)

#Define colors and fonts
light_gray = '#f3f3f3'
mid_gray =  '#6c8794'
dark_gray = '#4c5f65'
light_green = '#78dfc7'
white_green = '#edefe0'
dark_green = '#78dfc7'
button_font = ('Arial', 18)
display_font = ('Arial', 30)

#Define functions
def submit_number(number):
    """Add a number or decimal to display"""
    #insert the number or decimal pressed to the end of display
    display.insert(END, number)

    #if decimal was pressed, disable it so that it can't be pressed twice
    if "." in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    """Store the first number of the expression and the operation to be used"""
    global first_number
    global operation

    #Get the operator pressed and the current value of display. This is the number in the calculation
    operation = operator
    first_number = display.get()

    #Delete the value (first number) from the entry display
    display.delete(0,END)

    #Disable all operator buttons until equal or clear is pressed
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    #Return decimal button to normal state
    decimal_button.config(state=NORMAL)

def equal():
    """Run the stored operation for 2 numbers"""
    #Do the math
    if operation == 'add':
        value = float(first_number) + float(display.get())
    elif operation == 'subtract':
        value = float(first_number) - float(display.get())
    elif operation == 'multiply':
        value = float(first_number) * float(display.get())
    elif operation == 'divide':
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(display.get())
    
    #Remove current value of display (index 0:sta loppuun) and update with the answer
    display.delete(0,END)
    display.insert(0, value)

    #Return buttons to normal states
    enable_buttons()

def enable_buttons():
    """Enable all buttons"""
    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)

def clear():
    """Clear the display"""
    display.delete(0,END)
    #return buttons to normal state
    enable_buttons()

def inverse():
    """Calculate the inverse"""
    #Do not allow 1/0
    if display.get == "0":
        value = 'ERROR'
    elif not display.get == "0":
        value = 1/float(display.get())
    #remove current value and insert the answer to the display
    display.delete(0,END)
    display.insert(0,value)

def square():
    """Calculate the square of given number"""
    value = float(display.get())**2
    #remove current value and insert the answer to the display
    display.delete(0,END)
    display.insert(0,value)

def negate():
    """Calculate the negative value of given number"""
    value = -(float(display.get()))
    #remove current value and insert the answer to the display
    display.delete(0,END)
    display.insert(0,value)



#GUI layout
#Define frames
display_frame = tkinter.LabelFrame(root,)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5,20))
button_frame.pack(padx=2, pady=5)

#Layout for display frame
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=white_green, borderwidth=5, justify=RIGHT)
display.pack(padx=5,pady=5)

#Layout for button frame
clear_button = tkinter.Button(button_frame, text='Clear', font=button_font, bg=light_gray, command=clear)
quit_button = tkinter.Button(button_frame, text='Quit', font=button_font, bg=light_gray, command=root.destroy)

inverse_button = tkinter.Button(button_frame, text='1/x', font=button_font, bg=light_green, command=inverse)
square_button = tkinter.Button(button_frame, text='x^2', font=button_font, bg=light_green, command=square)
exponent_button = tkinter.Button(button_frame, text='x^n', font=button_font, bg=light_green, command=lambda:operate('exponent'))
divide_button = tkinter.Button(button_frame, text='/', font=button_font, bg=light_green, command=lambda:operate('divide'))
multiply_button = tkinter.Button(button_frame, text='*', font=button_font, bg=light_green, command=lambda:operate('multiply'))
subtract_button = tkinter.Button(button_frame, text='-', font=button_font, bg=light_green, command=lambda:operate('subtract'))
add_button = tkinter.Button(button_frame, text='+', font=button_font, bg=light_green, command=lambda:operate('add'))
equal_button = tkinter.Button(button_frame, text='=', font=button_font, bg=dark_green, command=equal)
decimal_button = tkinter.Button(button_frame, text='.', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number("."))
negate_button = tkinter.Button(button_frame, text='+/-', font=button_font, bg=mid_gray, fg='white', command=negate)

nine_button = tkinter.Button(button_frame, text='9', font=button_font, bg=mid_gray, fg='white', command=lambda: submit_number(9))
eight_button = tkinter.Button(button_frame, text='8', font=button_font, bg=mid_gray, fg='white', command=lambda: submit_number(8))
seven_button = tkinter.Button(button_frame, text='7', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(7))
sixsixsix_button = tkinter.Button(button_frame, text='6', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(6))
five_button = tkinter.Button(button_frame, text='5', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(5))
four_button = tkinter.Button(button_frame, text='4', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(4))
three_button = tkinter.Button(button_frame, text='3', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(3))
two_button = tkinter.Button(button_frame, text='2', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(2))
one_button = tkinter.Button(button_frame, text='1', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(1))
zero_button = tkinter.Button(button_frame, text='0', font=button_font, bg=mid_gray, fg='white',command=lambda: submit_number(0))

#first row
clear_button.grid(row=0,column=0,columnspan=2,pady=1,sticky='WE')
quit_button.grid(row=0,column=2,columnspan=2,pady=1, sticky="WE")
#second row
inverse_button.grid(row=1,column=0, pady=1, sticky='WE')
square_button.grid(row=1,column=1, pady=1, sticky='WE')
exponent_button.grid(row=1,column=2, pady=1, sticky='WE')
divide_button.grid(row=1,column=3, pady=1, sticky='WE')
#third row (add padding to create the size of column(,because size of column is dependent on the largest element in column))
seven_button.grid(row=2,column=0, pady=1, sticky='WE', ipadx=20)
eight_button.grid(row=2,column=1, pady=1, sticky='WE', ipadx=20)
nine_button.grid(row=2,column=2, pady=1, sticky='WE', ipadx=20)
multiply_button.grid(row=2,column=3, pady=1, sticky='WE', ipadx=20)
#fourth row
four_button.grid(row=3,column=0,pady=1, sticky='WE')
five_button.grid(row=3,column=1,pady=1, sticky='WE')
sixsixsix_button.grid(row=3,column=2,pady=1, sticky='WE')
subtract_button.grid(row=3,column=3,pady=1, sticky='WE')
#fifth row
one_button.grid(row=4,column=0,pady=1, sticky='WE')
two_button.grid(row=4,column=1,pady=1, sticky='WE')
three_button.grid(row=4,column=2,pady=1, sticky='WE')
add_button.grid(row=4,column=3,pady=1, sticky='WE')
#sixth row
negate_button.grid(row=6,column=0,pady=1, sticky='WE')
zero_button.grid(row=6,column=1,pady=1, sticky='WE')
decimal_button.grid(row=6,column=2,pady=1, sticky='WE')
equal_button.grid(row=6,column=3,pady=1, sticky='WE')

#Run main loop
root.mainloop()