import pyowm
from pyowm.utils.config import get_default_config


def weather_bot(city='Mogilev'):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    owm = pyowm.OWM('4838bcc4a7d6f997ba9f521bdfd85706')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather
    # temperature = w.temperature('celsius')['temp_min']
    # temperature_ad = w.temperature('celsius')["feels_like"]
    # rain = w.detailed_status
    # wind = w.wind()['speed']
    # humidity = w.humidity

    # text = f"Тэмпература зараз {temperature}°. Адчуваецца як {temperature_ad}°.\n" \
           # f"Воблачнасць: {rain} \n" \
           # f"Вецер: {wind} м/с\n" \
           # f"Вільготнасць: {humidity} "

    text = ("Тэмпература сення ад " + str(w.temperature('celsius')["temp_min"]) + "° да " + str(
        w.temperature('celsius')["temp_max"]) + "°. " +
            "Адчуваецца як " + str(w.temperature('celsius')["feels_like"]) + "°." + "\n" +
            "Воблачнасць: " + w.detailed_status + "\n" +
            "Вецер: " + str(w.wind()['speed']) + " метраў у секунду" + "\n" +
            'Вільготнасць: ' + str(w.humidity) + '%')

    return text
# weather_bot()


# print(weather_bot())
