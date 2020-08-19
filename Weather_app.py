import  tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import requests


root=tk.Tk()
root.title("WeatherApp")

HEIGHT=500
WIDTH=600

#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
#api.openweathermap.org/data/2.5/forecast?q={city name},{state code}&appid={your api key}
#api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}
#c7fac9f88d0f33e9abff2c834f3dc97f

def format_response(weather):
        try:
                name= weather['name']
                desc= weather['weather'][0]['description']
                temp= weather['main']['temp']

                final_str= 'City: %s \nConditions: %s \nTemperature(°C): %s'%(name,desc,temp)
        except:
                final_str= 'There was a problem retrieving that information'

        return final_str

def get_weather(city):
	weather_key='c7fac9f88d0f33e9abff2c834f3dc97f'
	url='https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':weather_key,'q':city, 'units':'metric'}
	response = requests.get(url,params=params)
	weather = response.json()
	
	label['text']=format_response(weather)
	
		
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
background_image= tk.PhotoImage(file='./landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()


frame=tk.Frame(root,bg='#7cded9',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=('Century',12))
entry.place(relwidth=0.65, relheight=1)

button=tk.Button(frame,text="GET WEATHER",font=('Century',12),command=lambda:get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)


lower_frame=tk.Frame(root,bg='#7cded9',bd=10)
lower_frame.place(anchor='n',relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6)


label=tk.Label(lower_frame,anchor='nw', justify='left', bd=4,font=('Century',12))
label.place(relwidth=1,relheight=1)

root.mainloop()
