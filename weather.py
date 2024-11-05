from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests
import geocoder

def open_intro_window():
    intro_window = Toplevel()
    intro_window.title("Welcome to Weather Whiz")
    intro_window.geometry("1350x700+0+0")

    Label(intro_window, text="Welcome to Weather Whiz!", font=("Helvetica", 30,"bold")).pack(pady=100)
    Button(intro_window, text="...Start...", font=("Helvetica", 17),bg="skyblue",
           command=lambda: [intro_window.destroy(), root.deiconify()]).pack(pady=20)

root = Tk()
root.title("WEATHER WHIZ")
root.geometry("1350x700+0+0")
root.withdraw()

api_key = "8e59bdb17d023eaaadd6a493827bbb60"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        wind_speed = wind['speed']
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        feels_like = main['feels_like']

        t.config(text=f"{temperature}°C")
        c.config(text=f"{city.capitalize()}")
        W.config(text=f"Wind speed: {wind_speed} m/s")
        H.config(text=f"{humidity}%")
        D.config(text=description.capitalize())
        P.config(text=f"{pressure} hPa")
        feels_like_label.config(text=f"Feels like: {feels_like}°C")
        return True
    else:
        messagebox.showerror("Error", "City not found.")
        return False

def show_weather_report():
    city = textfield.get()
    if city:
        if get_weather(city):
            # Create a new window for the weather report
            report_window = Toplevel(root)
            report_window.title("Weather Report")
            report_window.geometry("300x400")

            Label(report_window, text=f"Weather Report for {city}", font=("Helvetica", 16)).pack(pady=10)
            Button(report_window, text="Close", command=report_window.destroy, fg="skyblue").pack(pady=20)
    else:
        messagebox.showerror("Error", "Please enter a city name.")

def getWeather():
    city = textfield.get()
    if city:
        get_weather(city)
    else:
        messagebox.showerror("Error", "Please enter a city name.")

def get_current_location_weather():
    g = geocoder.ip('me')  # Get current location based on IP
    if g.ok and g.city:
        get_weather(g.city)
    else:
        messagebox.showerror("Error", "Could not determine current location. Please enter a city name.")

# Search box and layout setup
search_image = PhotoImage(file="C:/Users/Choice/OneDrive/Desktop/Weather App/images/searchbar.png")
myimage = Label(image=search_image)
myimage.place(x=11, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 30, "bold"), bg="lightgrey", border=0, fg="dimgrey")
textfield.place(x=90, y=70)
textfield.focus()

search_icon = PhotoImage(file="C:/Users/Choice/OneDrive/Desktop/Weather App/images/searchicon (2).png")
search_myimage = Label(image=search_icon, cursor="hand2", borderwidth=0, bg="#404040")
search_myimage.place(x=473, y=57)
search_myimage.bind("<Button-1>", lambda event: getWeather())

# Additional UI elements
Logo_image = PhotoImage(file="C:/Users/Choice/OneDrive/Desktop/Weather App/images/logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=130)

Frame_image = PhotoImage(file="C:/Users/Choice/OneDrive/Desktop/Weather App/images/lightblue (1).png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=tk.BOTTOM)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=100, y=540)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=400, y=540)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=690, y=540)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=950, y=540)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=700, y=250)
c = Label(font=("arial", 25, "bold"), fg="#ee666d")
c.place(x=700, y=150)

W = Label(text="...", font=("arial", 15, "bold"), bg="skyblue")
W.place(x=100, y=590)
H = Label(text="...", font=("arial", 15, "bold"), bg="skyblue")
H.place(x=400, y=590)
D = Label(text="...", font=("arial", 15, "bold"), bg="skyblue")
D.place(x=690, y=590)
P = Label(text="...", font=("arial", 15, "bold"), bg="skyblue")
P.place(x=950, y=590)

feels_like_label = Label(font=("arial", 15, "bold"))
feels_like_label.place(x=700, y=400)

# Fetch weather for current location at startup
get_current_location_weather()

# Open the introductory window
open_intro_window()

root.mainloop()
