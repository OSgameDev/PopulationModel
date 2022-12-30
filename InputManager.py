from models import Insect

class Manager:
    def __str__(self):
        return "This is the input manager class"

    def get_insect_int(self, name):
        valid = False

        while not valid:
            population = input(f"Enter {name} Population number: ")
            try:
                population = int(population)

                survival_rate = input(f"Enter {name} survival rate :")
                try:
                    survival_rate = int(survival_rate)
                    valid = True
                    return Insect(population, survival_rate)
                except:
                    print("Integer input expected!\n")
            except:
                print("Integer input expected!\n")

    def get_int(self, name):
        valid = False

        while not valid:
            number = input(f"Enter {name} number: ")
            try:
                number = int(number)
                valid = True
                return number
            except:
                print("Integer input expected!\n")

    def get_str(self, name):
        valid = False

        while not valid:
            string = input(f"Enter {name}: ")
            try:
                string = str(string)
                valid = True
                return string
            except:
                print("Integer input expected!\n")

    def get_y_or_n(self, question):
        valid = False

        while not valid:
            string = input(f"{question}").lower()
            if string == "y":
                return True
            elif string == "n":
                return False
            else:
                print("Invalid input!\n")

    def get_filename(self, outstring,extention):

        filename = self.get_str(f"{outstring}").lstrip()
        if not filename.endswith(extention):
            filename += extention
        elif filename.endswith("."):
            filename = filename.replace(".", extention)
        return filename
