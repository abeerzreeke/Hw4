import requests
import datetime

def weather():

    now = datetime.datetime.now()
    print("**Hello to WEATHER app**")

    try:
        year = int(input('Enter a year'))
        month = int(input('Enter a month'))
        day = int(input('Enter a day'))
        choose_date = datetime.datetime(year, month, day)
    except ValueError:
        print("cannot parse your date!")

    else:
        if ( year - now.year < 0 or year - now.year > 1 ):
            print("!!!-dont have info-!!!")
            return 0

        elif (month - now.month < 0 or month - now.month > 1):
            print("!!!-dont have info-!!!")
            return 0

        elif (day < now.day or day - now.day > 10):
            print("-dont have info-")
            return 0

    City = input("Enter City")
    #check if the input without numbers
    a = any(str.isdigit(c) for c in City)
    if a:
        print("Don't put numbers in your City!")
    else:
        print("**************")

    #The URL we want to make the request to
    #In end of the url about what the user input
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=ca906cb4997343508e7165953202010&q={City}")
    #data we received back from the API
    pass_times = response.json()
    #to see the data
    #print(pass_times)

    location = pass_times["location"]
    current = pass_times["current"]

    print(f'The Temperature\n In date {choose_date}\n In {location["name"]}\n Is: {current["temp_c"]} \n\n This is correct for date: {location["localtime"]}')

if __name__ == '__main__':
    weather()

