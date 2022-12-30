import sys
import os
from calculations import Calculations
from InputManager import Manager
from Exporter import ExcelExporter
from models import Insect

input_manager = Manager()
exporter = ExcelExporter()

Juvenile = Insect(0, 0)
Adults = Insect(0, 0)
Seniles = Insect(0, 0)

generations_number = 0
birth_rate = 0
disease_trigger_point = 0

data_list = []

def export():
    global data_list
    filename = input_manager.get_filename("filename", ".xls")
    if os.path.exists(filename):
        overwrite = input_manager.get_y_or_n(f"A file with the name ({filename}) already exist. Do you want to overwrite [Y] [N]: ")
        if overwrite:
            exporter.export_data(filename, data_list)
        else:
            export()
    else:
        exporter.export_data(filename, data_list)

while True:
    print("""
            1- Set values
            2- Show data list
            3- Export data list
            4- exit
        """)

    choice = input_manager.get_int("Choice")

    if choice == 1:
        Juvenile = input_manager.get_insect_int("Juveniles")
        Adults = input_manager.get_insect_int("Adults")
        Seniles = input_manager.get_insect_int("Seniles")
        generations_number = input_manager.get_int("generations")
        birth_rate = input_manager.get_int("birth rate")
        disease_trigger_point = input_manager.get_int("disease factor trigger point")

        calculator = Calculations(Juvenile, Adults, Seniles, birth_rate, generations_number, disease_trigger_point)
        data_list = calculator.calculate_generations_to_list()

        print("\nValues set\n")

    if choice == 2:
        for data in data_list:
            print(f"{data}\n")

    if choice == 3:
        export()

    if choice == 4:
        sys.exit()

    if choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("Invalid choice!\n")