from urllib.request import urlopen


MAIN_URL = "https://wetter.orf.at/oes/"


def decode_website(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html


def get_temperature_from_city(cityname):
    html = decode_website(MAIN_URL)
    index_of_city_name = html.find("<h3 itemprop=\"name\">" + cityname + "</h3>")
    characters_before_temperature = 58
    length_of_html_p_element = index_of_city_name+characters_before_temperature+len(cityname)
    temperature = html[length_of_html_p_element:length_of_html_p_element+4]
    return float(temperature.replace(",", "."))


def get_measurement_time_from_main_page():
    html = decode_website(MAIN_URL)
    last_measurement_text = "Letzte Messwerte von "
    index_of_measurement_time = html.find(last_measurement_text)
    length_of_text_before_time = index_of_measurement_time + len(last_measurement_text)
    measurement_time = html[length_of_text_before_time:length_of_text_before_time+5]
    return str(measurement_time)


