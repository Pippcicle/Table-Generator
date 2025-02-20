from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('Multiplication Table')

main_heading = Label(window, text= ' Multiplication Table', font= ('comic sans',16 , 'bold'))
main_heading.grid( row = 0, column = 0, columnspan = 3, pady = 25)

range_lbl = Label(window, text= ' Number and Range : ', font = ('comic sans', 13, 'bold'))
range_lbl.grid( row = 1, column = 0, padx = 10)

#combobox creation
num = IntVar()
drop_down = Combobox(window, textvariable = num, width = 5, state = 'readonly')
drop_down['values'] = tuple(range(101))
drop_down.grid( row = 1, column = 1)

#radiobuttons creation
endval  = IntVar()
r10 = Radiobutton(window, text = '10', variable = endval, value = 10)
r20 = Radiobutton(window, text = '20', variable = endval, value = 20)
r30 = Radiobutton(window, text = '30', variable = endval, value = 30)
endval.set(10)

r10.grid( row = 1, column = 2)
r20.grid( row = 2, column = 2, padx = 30)
r30.grid( row = 3, column = 2, padx = 30)

def generate_table():
    tables = ""

    for i in range(1, endval.get() + 1):
        mult = num.get() * i
        tables += str(num.get()) + " X " + str(i) + " = " + str(mult) + "\n"
    table.configure(text = tables)

generate = Button( window, text = 'generate', command = generate_table)
generate.grid( row = 4, column = 1)

table = Label(window, anchor = 'center')
table.grid( row = 5, column = 1, pady = 25)

window.mainloop()