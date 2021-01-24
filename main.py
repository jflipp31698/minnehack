import tkinter as tk
from sinbad import *
import random


def makeMilagePage(a):
    print(a)

def clear_entry(event, entry):
    entry.delete(0, tk.END)

def getMileage(year, make, model):

    ds = DataSource.connect("http://www.fueleconomy.gov/ws/rest/vehicle/menu/options", format="xml")
    ds.set_param("year", str(year))
    ds.set_param("make", make).set_param("model", model)
    ds.load()
    vehicle_id = ds.fetch()[0]['value']
    vehicle_data = "https://www.fueleconomy.gov/ws/rest/vehicle/" + vehicle_id
    ds = DataSource.connect(vehicle_data, format="xml")
    ds.load()
    mileage = ds.fetch("comb08U")

    if (mileage == "0.0"):
        return random.randint(20, 40)
    else:
        return mileage
    


def openNewWindow(master): 
    master.destroy()
    newWindow = tk.Tk() 
    newWindow.geometry("500x400")
    newWindow.title("Car Adder")
    newWindow.resizable(False, False)
    bgLabel = tk.Label(newWindow, bg="#d2fdff")
    bgLabel.place(relheight=1, relwidth=1)
    entry = tk.Entry(newWindow, borderwidth = 0, highlightthickness = 0)
    entry.insert(0, "        Year")
    entry.place(relheight=0.1, relwidth=0.5, relx = 0.3, rely= 0.2)
    entry.bind("<Button-1>", lambda event: clear_entry(event, entry))
    entry1 = tk.Entry(newWindow, borderwidth = 0, highlightthickness = 0)
    entry1.insert(0, "        Make")
    entry1.place(relheight=0.1, relwidth=0.5, relx = 0.3, rely= 0.4)
    entry1.bind("<Button-1>", lambda event: clear_entry(event, entry1))
    entry2 = tk.Entry(newWindow, borderwidth = 0, highlightthickness = 0)
    entry2.insert(0, "        Model")
    entry2.place(relheight=0.1, relwidth=0.5, relx = 0.3, rely= 0.6)
    entry2.bind("<Button-1>", lambda event: clear_entry(event, entry2))
    submitButton = tk.Button(newWindow, borderwidth = 0,highlightthickness = 0, text = "get mileage", command=lambda:print(makeMilagePage(getMileage(entry.get(), entry1.get(), entry2.get()))))
    submitButton.place(relheight = 0.1, relwidth = 0.3, relx = 0.3, rely = 0.8)

    newWindow.mainloop()

root = tk.Tk()
root.geometry("960x540")
root.title("Car Emission Tracker")
root.resizable(False, False)
bgLabel = tk.Label(root, bg="#d2fdff")
bgLabel.place(relheight=1, relwidth=1)

addButton = tk.Button(root,borderwidth = 0, highlightthickness = 0, text = 'add vehicle', command=lambda:openNewWindow(root))
addButton.place(relx=0.8, rely= 0.8, relwidth = 0.1, relheight = 0.06)
root.mainloop() 