


from tkinter import *
import parser





root = Tk()
root.title("GUI based Calcalutor")

root.configure(background="light green") 
root.geometry("685x300")
i = 0
def take_input(num):
    global i
    display.insert(i,num)
    i+=1

def take_operator(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length


def calculate():
    entire_string = display.get()
    try:
        result = parser.expr(entire_string).compile()
        new_result = eval(result)
        clear_all()
        display.insert(0, new_result)
    except:
        clear_all()
        display.insert(0,"ZERO DIVISION ERROR")
    
def clear_all():
    display.delete(0,END)
    
def single_delete():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0,"Screen is Already Cleared!!!!")
        

display = Entry(root,font=("Helvetica", 20),width=100)
display.grid(row=0, column=0, columnspan=30)
Button(root,text="1",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12), command = lambda: take_input(1)).grid(row=1,column=0)
Button(root,text="2",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_input(2)).grid(row=1,column=1)
Button(root,text="3",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_input(3)).grid(row=1,column=2)
Button(root,text="+",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("+")).grid(row=1,column=3)
Button(root,text="pie",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("*3.14")).grid(row=1,column=4)
Button(root,text="Delete",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: single_delete()).grid(row=1,column=5)

Button(root,text="4",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_input(4)).grid(row=2,column=0)
Button(root,text="5",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_input(5)).grid(row=2,column=1)
Button(root,text="6",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12), command = lambda: take_input(6)).grid(row=2,column=2)
Button(root,text="-",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("-")).grid(row=2,column=3)
Button(root,text="%",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("%")).grid(row=2,column=4)
Button(root,text=".",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12), command = lambda: take_operator(".")).grid(row=2,column=5)


Button(root,text="7",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_input(7)).grid(row=3,column=0)
Button(root,text="8",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12), command = lambda: take_input(8)).grid(row=3,column=1)
Button(root,text="9",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_input(9)).grid(row=3,column=2)
Button(root,text="*",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("*")).grid(row=3,column=3)
Button(root,text="(",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("(")).grid(row=3,column=4)
Button(root,text=")",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator(")")).grid(row=3,column=5)

Button(root,text="AC",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12), command = lambda: clear_all()).grid(row=4,column = 0)
Button(root,text="0",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_input(0)).grid(row=4,column=1)
Button(root,text="=",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: calculate()).grid(row=4,column=2)
Button(root,text="/",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("/")).grid(row=4,column=3)
Button(root,text="exp",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("**")).grid(row=4,column=4)
Button(root,text="^2",fg='black', bg='yellow',height=1, width=6,padx=10, pady=10,font=("Helvetica", 12),command = lambda: take_operator("**2")).grid(row=4,column=5)

root.mainloop()







