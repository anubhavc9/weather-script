import pyowm


def main():
    city = input("Enter city name: ")
    # copy paste your API key in the empty single quotes in the following line of code
    owm = pyowm.OWM('')
    location = owm.weather_at_place(city)
    weather = location.get_weather()

    temp = weather.get_temperature('celsius')
    humidity = weather.get_humidity()
    pressure = weather.get_pressure()
    wind = weather.get_wind()

    print("Description:",weather.get_detailed_status())
    print("Temperature:",str(temp['temp'])+"°C")
    print("Minimum temperature:",str(temp['temp_min'])+" °C")
    print("Maximum temperature:",str(temp['temp_max'])+" °C")
    print("Humidity:",str(humidity)+' %')
    print("Pressure:",str(pressure['press'])+" millibar")
    print("Wind speed:",str(wind['speed'])+" mph")


if __name__ == "__main__":
    main()