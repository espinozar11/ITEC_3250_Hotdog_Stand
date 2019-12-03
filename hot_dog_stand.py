import tkinter as tk
import datetime
from tkinter import messagebox


def open_application():

    window = tk.Tk()
    window.title("Hot Dog World")
    window.tk_setPalette(background='#F8F8F8', foreground='black',
                activeBackground='#C0C0C0', activeForeground='#F8F8F8')

    # create dimensions of window- half of screen width & height
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry('%sx%s' % (int(width/1.5), int(height/1.5)))

    # create GUI itself
    cal_profit_date = tk.StringVar()
    numb_of_hotdogs = tk.IntVar()
    sale_date = datetime.date.today()
    price = tk.DoubleVar()
    tk.Label(window, text="The Hotdog World", font=("Eras Bold ITC", 30), background="#90ee90", width=40,
                  height=2).grid(row=0,columnspan=2)
    tk.Button(window, text="Calculate Total Profit", command=calculate_total_profit).grid(row=1,columnspan=2)
    tk.Entry(window, textvariable=cal_profit_date).grid(sticky="E",row=2, column=0, padx=15)
    tk.Button(window, text="Calculate Day Profit", command=lambda: calculate_day_total(cal_profit_date.get())).grid(sticky="W", row=2,column=1)

    tk.Label(window, text="Number of Hot Dogs").grid(sticky="E",row=3, column=0, padx=15)
    tk.Entry(window, textvariable=numb_of_hotdogs).grid(sticky="W", row=3, column=1)

    tk.Label(window, text="Sale Date").grid(sticky="E", row=4, column=0, padx=15)
    tk.Label(window, text=sale_date).grid(sticky="W",row=4, column=1)

    tk.Label(window, text="Sale Price").grid(sticky="E", row=5, column=0, padx=15)
    tk.Entry(window, textvariable=price).grid(sticky="W", row=5, column=1)

    tk.Button(window, text="Add Hot Dog Order", command=lambda: add_sale(numb_of_hotdogs.get(), sale_date.get(), price.get())).grid(row=6,columnspan=2)

    window.grid()
    window.mainloop()


def add_sale(num_of_hotdogs, sale_date, price):
    """this will add the sale to the file"""

    return 'Sale has been added successfully!'


def calculate_total_profit():
    """reads file and calculates total profit"""
    total_profit = 0
    tk.messagebox.showinfo("Hot Dog World | Total Profit", "The total profits are: " + str(total_profit))
    return total_profit


def calculate_day_total(day):
    """reads file and calculates the total profit for that day"""
    day_total_profit = 0
    tk.messagebox.showinfo("Hot Dog World | Day Total Profit", "The total profits for " + day + " are: " + str(day_total_profit))
    return day_total_profit


if __name__ == '__main__':
    open_application()
