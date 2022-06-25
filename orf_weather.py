import view
import datahandler


def show_main_menu():
    view.clear_screen()
    view.print_cloud_logo()
    view.print_message("Austrian weather // ORF Wetter Web Scraper")
    main_menu_list = ["Average temperature in Austria right now",
                      "Temperatures in Austrian regional capital cities"]
    view.print_selection(main_menu_list)
    user_selection = view.get_user_input("Choose your selection by number: ")
    view.print_message(user_selection)


if __name__ == "__main__":
    show_main_menu()