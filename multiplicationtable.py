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









window.mainloop()