from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active

sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["A2"] = "Alice"
sheet["B2"] = "25"
sheet["A3"] = "Bob"
sheet["B3"] = "30"

workbook.save("Sample.xlsx")
print("Exel File Created Succesfully")