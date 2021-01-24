import tkinter as tk
from tkinter import font
from sinbad import *

def makeMilagePage(root, miles, window, mileage):
    window.destroy()
    your_mpg = tk.Label(root, text="Your vehicles miles per gallon is " + mileage + " MPG", font="Arial 16", bg="#d2fdff")
    your_mpg.place(relx=0, rely=0.15, relheight=0.1, relwidth=1)

    weekly_miles = tk.Label(root, text=" During the week you drove " + miles + " miles", font="Arial 16", bg="#d2fdff")
    weekly_miles.place(relx=0, rely=0.3, relheight=0.1, relwidth=1)

    gallons_per_week = round(int(miles)/int(mileage), 2)
    emissions = round((19.6 * gallons_per_week), 2)
    gallons_used = tk.Label(root, text=" This means you used " + str(gallons_per_week) + " gallons\n and you emitted " + str(emissions) + " pounds of CO2 into the atmosphere!", font="Arial 16", bg="#d2fdff")
    gallons_used.place(relx=0, rely=0.45, relheight=0.1, relwidth=1)

    avg_yearly_emissions = 10141.3
    avg_weekly_emissions = avg_yearly_emissions/52
    emissions_score = round(emissions/avg_weekly_emissions, 2)

    percent = " "

    if 1 - emissions_score < 0:
        percent = "You emit " + str((1 - emissions_score) * -100) + "% more CO2 than the average American driver!"
    elif 1 - emissions_score == 0:
        percent = "You are exactly average! (YAY)"
    else:
        percent = "You emit " + str((1-emissions_score) * 100) + "% less CO2 than the average American driver"



    emissions_score_label = tk.Label(root, text=percent, font="Arial 16", bg="#d2fdff")
    emissions_score_label.place(relx=0, rely=0.6, relheight=0.1, relwidth=1)


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
    mileage = ds.fetch("comb08")

    return mileage
    


def openNewWindow(master): 
    newWindow = tk.Tk() 
    newWindow.geometry("500x400")
    newWindow.title("Car Adder")
    newWindow.resizable(False, False)

    bgLabel = tk.Label(newWindow, bg="#d2fdff")
    bgLabel.place(relheight=1, relwidth=1)

    entry = tk.Entry(newWindow, borderwidth = 0, highlightthickness = 0)
    entry.insert(0, "        Year")
    entry.place(relheight=0.1, relwidth=0.3, relx = 0.1, rely= 0.2)
    entry.bind("<Button-1>", lambda event: clear_entry(event, entry))

    entry1 = tk.Entry(newWindow, borderwidth = 0, highlightthickness = 0)
    entry1.insert(0, "        Make")
    entry1.place(relheight=0.1, relwidth=0.3, relx = 0.1, rely= 0.4)
    entry1.bind("<Button-1>", lambda event: clear_entry(event, entry1))

    entry2 = tk.Entry(newWindow, borderwidth = 0, highlightthickness = 0)
    entry2.insert(0, "        Model")
    entry2.place(relheight=0.1, relwidth=0.3, relx = 0.1, rely= 0.6)
    entry2.bind("<Button-1>", lambda event: clear_entry(event, entry2))

    entry3 = tk.Entry(newWindow, borderwidth = 0, highlightthickness = 0)
    entry3.insert(0, "        Weekly Miles Driven")
    entry3.place(relheight=0.1, relwidth=0.3, relx = 0.5, rely= 0.4)
    entry3.bind("<Button-1>", lambda event: clear_entry(event, entry3))
    submitButton = tk.Button(newWindow, borderwidth = 0,highlightthickness = 0, text = "get mileage", command=lambda:makeMilagePage(master, entry3.get(), newWindow, getMileage(entry.get(), entry1.get(), entry2.get())))
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