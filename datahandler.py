import scraper
import view

AUSTRIAN_REGIONAL_CAPITALS = ["Wien", "St. P&ouml;lten", "Eisenstadt", "Graz",
                              "Linz", "Klagenfurt", "Salzburg", "Innsbruck",
                              "Bregenz"]


def get_average_temperature_of_country():
    city_temperature_sum = 0
    view.print_waiting_message()
    for city in AUSTRIAN_REGIONAL_CAPITALS:
        city_temperature_sum += scraper.get_temperature_from_city(city)
    view.clear_screen()
    return str(city_temperature_sum / len(AUSTRIAN_REGIONAL_CAPITALS))[0:5]


def get_temperature_of_city(city_index):
    view.print_waiting_message()
    chosen_city = AUSTRIAN_REGIONAL_CAPITALS[city_index]
    city_temperature = scraper.get_temperature_from_city(chosen_city)
    view.clear_screen()
    return str(city_temperature)[0:5]


def get_time_of_last_measurement():
    time = scraper.get_measurement_time_from_main_page()
    return time