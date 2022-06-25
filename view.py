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


def get_user_input(label):
    return input(label)