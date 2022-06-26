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


def get_temperatures_for_all_cities():
    temperature_dict = {}
    for index, city in enumerate(AUSTRIAN_REGIONAL_CAPITALS):
        temperature_dict[city] = float(get_temperature_of_city(index))
    return temperature_dict


def get_city_with_highest_temperature():
    temperature_dict = get_temperatures_for_all_cities()
    hottest_cities_dict = {}
    highest_temp = 0
    for key in temperature_dict:
        if temperature_dict[key] > highest_temp:
            highest_temp = temperature_dict[key]
            hottest_cities_dict = {}
            hottest_cities_dict[key] = temperature_dict[key]
        elif temperature_dict[key] == highest_temp:
            hottest_cities_dict[key] = temperature_dict[key]
    return hottest_cities_dict


def get_time_of_last_measurement():
    time = scraper.get_measurement_time_from_main_page()
    return time


get_city_with_highest_temperature()