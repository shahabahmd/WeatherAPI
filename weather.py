from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

API_KEY = "c82fecb677c74bbd0d4502704125ed7b"

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getWeather():
    try:
        city = textfield.get()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geo_url, timeout=5)
        geo_data = geo_response.json()

        if not geo_data:
            messagebox.showerror("Error", f"City '{city}' not found.")
            return

        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lon, lat=lat)
        if result is None:
            messagebox.showerror("Error", "Could not determine timezone.")
            return

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_data = requests.get(weather_url, timeout=5).json()

        condition = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temp = int(weather_data['main']['temp'])
        feels_like = int(weather_data['main']['feels_like'])
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        wind = weather_data['wind']['speed']

        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | FEELS LIKE {feels_like}°C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description)
        p.config(text=f"{pressure} hPa")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
Search_image = PhotoImage(file="Copy of search.png")
myimage = tk.Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = tk.Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

Logo_image = PhotoImage(file="Copy of logo.png")
logo = tk.Label(image=Logo_image)
logo.place(x=150, y=100)

Frame_image = PhotoImage(file="Copy of box.png")
frame_myimage = tk.Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=tk.BOTTOM)

name = tk.Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = tk.Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Static Labels
label1 = tk.Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Dynamic Labels
t = tk.Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = tk.Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)

p = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=650, y=430)

root.mainloop()