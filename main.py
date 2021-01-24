from tkinter import * 
from sinbad import *

ds = DataSource.connect("http://www.fueleconomy.gov/ws/rest/vehicle/menu/options", format="xml")
ds.set_param("year", "2011")
ds.set_param("make", "Toyota").set_param("model", "Camry")
ds.load()
try:
    print(ds.fetch()[0]['value'])
except Exception as e:
    print("Couldn't retrieve data.")







window = Tk()
window.geometry("960x540")
window.title("Car Emission Tracker")
window.resizable(False, False)
window.mainloop() 