REGIONAL_CAPITALS_SHORT = ["WIE", "STPÖ", "EISENSTD", "GRAZ",
                           "LINZ", "KLGFT", "SLZBRG", "INNSBR",
                           "BRGNZ"]


def clear_screen():
    print("\033c")


def print_cloud_logo():
    print('''          .-~~~-.
  .- ~ ~-(       )_ _
 /                    ~ -.
|                          ',
 \                         .'
   ~- ._ ,. ,.,.,., ,.. -~
           '       ''')


def print_message(message):
    print(message)


def print_selection(list_of_selection_items):
    print("\n")
    for index, item in enumerate(list_of_selection_items):
        print(f"{index}: {item}")
    print("\n")


def print_city_and_temperature_dict(label, dictionary):
    print(label)
    # Dict Format: {"Klagenfurt": 20.1}
    for key in dictionary:
        print(f"{key}: {dictionary[key]}")


def get_user_input(label):
    return input(label)


def print_temperature_graph(dictionary):
    temperature_list = [dictionary[key] for key in dictionary]
    max_temp = int(max(temperature_list))
    min_temp = int(min(temperature_list))
    table_list = []
    for _ in range(min_temp, max_temp+1):
        table_list.append([" ", " ", " ", " ", " ", " ", " ", " ", " "])
    counter = 0
    for temperature in temperature_list:
        index = temperature - min_temp
        table_list[int(index)][counter] = "X"
        table_list[int(index)].append(REGIONAL_CAPITALS_SHORT[counter])
        counter += 1
    table_list.reverse()
    print("Highest: " + str(max_temp) + " - " + str(max_temp+1) + "°C")
    for row in table_list:
        print("  ".join(row))
    print("Lowest: " + str(min_temp) + " - " + str(min_temp+1) + "°C")


def print_line_breaker():
    print("")
    print("- - - - - - - - - - - -")
    print("")


def input_to_continue():
    input("Press Enter to continue...")


def print_waiting_message():
    print("Getting data from wetter.orf.at ...")