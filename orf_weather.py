import view
import datahandler


AUSTRIAN_REGIONAL_CAPITALS = ["Wien", "St. Pölten", "Eisenstadt", "Graz",
                              "Linz", "Klagenfurt", "Salzburg", "Innsbruck",
                              "Bregenz"]


def show_main_menu():
    view.clear_screen()
    view.print_cloud_logo()
    view.print_message("Austrian weather // ORF Wetter Web Scraper")
    main_menu_list = ["Average temperature in Austria right now",
                      "Temperatures in Austrian regional capital cities",
                      "City with highest temperature right now",
                      "Temperature Graph"]
    view.print_selection(main_menu_list)


def show_average_temperature():
    view.clear_screen()
    average_temperature = datahandler.get_average_temperature_of_country()
    view.print_message(f"The average temperature in Austria: {average_temperature} °C.")
    measurement_time = datahandler.get_time_of_last_measurement()
    view.print_message(f"Time of measurement: {measurement_time}.")


def show_temperature_in_austrian_regional_city():
    view.clear_screen()
    view.print_selection(AUSTRIAN_REGIONAL_CAPITALS)
    user_selection = view.get_user_input("Choose your selection by number: ")
    user_selection = int(user_selection)
    city_temperature = datahandler.get_temperature_of_city(user_selection)
    view.print_message(f"The temperature in {AUSTRIAN_REGIONAL_CAPITALS[user_selection]}: {city_temperature}.")
    measurement_time = datahandler.get_time_of_last_measurement()
    view.print_message(f"Time of measurement: {measurement_time}.")


def show_city_with_highest_temperature():
    view.clear_screen()
    hottest_cities_dict = datahandler.get_city_with_highest_temperature()
    all_cities_dict = datahandler.get_temperatures_for_all_cities()
    view.print_city_and_temperature_dict("Hottest city/cities:", hottest_cities_dict)
    view.print_line_breaker()
    view.print_temperature_graph(all_cities_dict)
    view.print_line_breaker()


def show_temperature_graph():
    view.clear_screen()
    all_cities_dict = datahandler.get_temperatures_for_all_cities()
    view.print_temperature_graph(all_cities_dict)


if __name__ == "__main__":
    while True:
        show_main_menu()
        user_selection = view.get_user_input("Choose your selection by number: ")
        if user_selection == "0":
            show_average_temperature()
        elif user_selection == "1":
            show_temperature_in_austrian_regional_city()
        elif user_selection == "2":
            show_city_with_highest_temperature()
        elif user_selection == "3":
            show_temperature_graph()
        view.input_to_continue()