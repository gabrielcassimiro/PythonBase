import os
import platform
import api_requests as api
import customtkinter_projects.agenda_gui as agenda
import list
import oop
from utils import Decorators as dec, Iterators as it, Yields as y

running = True

while running:
    print("Choose an option below to see the example")
    print("1. Requests")
    print("2. List")
    print("3. OOP")
    print("4. Decorators")
    print("5. Iterators")
    print("6. Yields")
    print("7. CustomTkinter")
    print("0. exit: Exit the program")
    try:
        user_input = input("Select an option:")
        if user_input == "0":
            running = False
        elif user_input == "1":
            api.requests_examples()
        elif user_input == "2":
            list.list_examples()
        elif user_input == "3":
            oop.opp_examples()
        elif user_input == "4":
            dec.hello()
        elif user_input == "5":
            it.interator_example()
        elif user_input == "6":
            for num in y.yield_example(10):
                print(num)
        elif user_input == "7":
            app = agenda.App()
            app.mainloop()

    except ValueError:
        print("Invalid input")
        pass
    pass
