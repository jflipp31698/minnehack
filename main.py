from tkinter import * 
from sinbad import *

ds = DataSource.connect("http://www.fueleconomy.gov/ws/rest/vehicle/menu/options", format="xml")
ds.set_param("year", "2020")
ds.set_param("make", "Toyota").set_param("model", "Camry")
ds.load()
vehicle_id = ds.fetch()[0]['value']
vehicle_data = "https://www.fueleconomy.gov/ws/rest/vehicle/" + vehicle_id
ds = DataSource.connect(vehicle_data, format="xml")
ds.load()
mileage = ds.fetch("comb08U")


print(mileage)


window = Tk()
window.geometry("960x540")
window.title("Car Emission Tracker")
window.resizable(False, False)
window.mainloop() 