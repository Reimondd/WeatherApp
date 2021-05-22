import requests
from json import *
import os
import time
print("Welcome to Reimond's weather app!")
time.sleep(1)
os.system('cls')
while True:
    print("""
I - Info
W - Weather
C - Clear screen
Q - Quit program
    """)
    choice = input("> ").upper()
    if choice == "I":
        os.system('cls')
        print("Weather application using weatherstack's API")
        time.sleep(1)
        pass
    elif choice == "W":
        #Ask for the name of the city you want details of
        city = input("City name: ")
        # "opens" a url with my token and city name
        url = f"""http://api.weatherstack.com/current?access_key=1eaa0ab86878a13ba045ed5a71bebdeb&query={city}"""
        a = requests.get(url)         # i dont really know how to explain the next parts
        c = a.json() # It does something cant really explain
        # searches the items i specified in the brackets about the city
        desc = ["weather_descriptions"][0]
        country = c["location"]["country"]
        temp = c['current']['temperature']
        datetimes = c["location"]["localtime"]
        wind = c["current"]["wind_speed"]
        winddir = c["current"]["wind_dir"]
        print("The temperature in "+country+', ' +city+" is "+ str(temp) + " degrees Celcius")
        print("Weather status: "+desc)
        print("Wind direction= " +winddir+" and the wind is going "+ str(wind)+" km/h")
        print("Time: "+datetimes)
        time.sleep(2)
        pass
    elif choice == "Q":
        while True:
            print("Are you sure you wan to Quit? (Y)es/(N)o")
            quit = input("> ").upper()
            if quit == "Y":
                print("Goodbye!")
                time.sleep(1)
                exit()
            elif quit == "N":
                break
            else:
                print("I dont understand")
                time.sleep(1)
                os.system('cls')
                pass
    elif choice == "C":
        print("Clearing screen")
        time.sleep(1)
        os.system('cls')
        pass

    else:
        print("I dont understand")
        pass
