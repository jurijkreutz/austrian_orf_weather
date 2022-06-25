from urllib.request import urlopen


MAIN_URL = "https://wetter.orf.at/oes/"


def decode_website(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html


def get_temperature_from_city(cityname):
    html = decode_website(MAIN_URL)
    div_index = html.find("<h3 itemprop=\"name\">" + cityname + "</h3>")
    characters_before_temperature = 58
    length_of_html_p_element = div_index+characters_before_temperature+len(cityname)
    temperature = html[length_of_html_p_element:length_of_html_p_element+4]
    return float(temperature.replace(",", "."))