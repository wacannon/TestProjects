from urllib2 import Request, urlopen, URLError
import json
import datetime


def getdailyforecast():
    request = Request('http://api.openweathermap.org/data/2.5/forecast/daily?q=46517,us&cnt=7&mode=json&appid=72247a4769954dca379fd7e128dbe4b3&units=imperial')

    try:
        response = urlopen(request)
        data = json.load(response)
    except URLError, e:
        print 'Error', e

    city = data['city']['name']
    days = data['list']
    return days
    # print "Weather for: ", city
    # for day in days:
    #     date = datetime.datetime.fromtimestamp(int(day['dt'])).strftime('%m-%d')
    #     weather = day['weather'][0]['description']
    #     maxtemp = day['temp']['max']
    #     mintemp = day['temp']['min']
    #     humidity = day['humidity']
    #     windspeed = day['speed']
    #     return date, " Weather:", weather, " Max:", maxtemp, " Min:", mintemp, " Humidity:", humidity, " Wind:", windspeed, "mph"
