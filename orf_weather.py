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
                      "Temperatures in Austrian regional capital cities"]
    view.print_selection(main_menu_list)


def show_average_temperature():
    view.clear_screen()
    average_temperature = datahandler.get_average_temperature_of_country()
    view.print_message(f"The average temperature in Austria: {average_temperature} °C.")


def show_temperature_in_austrian_regional_city():
    view.clear_screen()
    view.print_selection(AUSTRIAN_REGIONAL_CAPITALS)
    user_selection = view.get_user_input("Choose your selection by number: ")
    user_selection = int(user_selection)
    city_temperature = datahandler.get_temperature_of_city(user_selection)
    view.print_message(f"The temperature in {AUSTRIAN_REGIONAL_CAPITALS[user_selection]}: {city_temperature}.")


if __name__ == "__main__":
    while True:
        show_main_menu()
        user_selection = view.get_user_input("Choose your selection by number: ")
        if user_selection == "0":
            show_average_temperature()
        elif user_selection == "1":
            show_temperature_in_austrian_regional_city()
        view.input_to_continue()