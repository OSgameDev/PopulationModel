import xlwt

class ExcelExporter:
    def __str__(self):
        return "This class exports data_list to excel spreadsheet"

    def export_data(self, filename, data_list):

        book = xlwt.Workbook(encoding="utf-8")

        sheet1 = book.add_sheet("Population Model Data")

        sheet1.write(0, 0, "Generation")
        sheet1.write(0, 1, "Juvenile")
        sheet1.write(0, 2, "Adult")
        sheet1.write(0, 3, "Senile")
        sheet1.write(0, 4, "Total")
        sheet1.write(0, 6, "Birthrate")
        sheet1.write(0, 7, data_list[0].birth_rate)

        i = 0
        for data in data_list:
            i = i + 1
            sheet1.write(i, 0, data.generation)
            sheet1.write(i, 1, data.juvenile_population)
            sheet1.write(i, 2, data.adult_population)
            sheet1.write(i, 3, data.senile_population)
            sheet1.write(i, 4, data.juvenile_population + data.adult_population + data.senile_population)

        try:
            book.save(f"{filename}")
        except:
            print("There was an error saving file")