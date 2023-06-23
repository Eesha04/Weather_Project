from tkinter import *                                               #importing all functions from tkinter
import tkinter as tk                                                #importing tkinter with some acronym which can be used to create an instance of widgets
from geopy.geocoders import Nominatim                             #geopy/geocoding-locate co-ordinates of addresses etc, nominatim - tool to search address
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
#from colorama import Fore

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getweather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent= "geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I : %M %p")
        clock.config(text=current_time)
        name.config(text= "CURRENT WEATHER")
        # Weather
        api = "https://api.openweathermap.org/data/2.5/weather?q= " +city+ "&appid=fdae55e9e368e6b2a825cee61bddaf93"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp ,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry !!")

#search box
Search_image = PhotoImage(file = "search.png")
myimage = Label(image = Search_image)
myimage.place(x = 20, y = 20)

textfield = tk.Entry(root, justify='center', width=17, font=(" poppins ", 25, " bold "), bg = '#404040', border = 0, fg = 'white')
textfield.place(x = 50, y = 40)
textfield.focus()

search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image = search_icon, borderwidth = 0, cursor = "hand2",bg='#404040',command=getweather)
myimage_icon.place(x =400, y = 34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#bottom box
frame_image = PhotoImage(file = "box.png")
frame_myImage = Label(image = frame_image)
frame_myImage.pack(padx = 5, pady = 5, side = BOTTOM)

#time
name =Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg='gray1',bg='orange')
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg='gray1',bg='orange')
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg='gray1',bg='orange')
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg='gray1',bg='orange')
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg='#ee666d')    #temperature
t.place(x=400,y=150)

c=Label(font=("arial",15,"bold"))                #condition
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg='#1ab5ef')    #wind
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg='#1ab5ef')    #humidity
h.place(x=280,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg='#1ab5ef')    #description
d.place(x=450,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg='#1ab5ef')     #pressure
p.place(x=670,y=430)


root.mainloop()