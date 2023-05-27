from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

bill_amount = float(input("Hey user, enter the bill amount: "))
bill_period = input("What is the bill period? (i.e. December 2021): ")

flatmate1_name = input("What's the name of the 1st flatmate? ")
days_in_house_flatmate1 = int(input(f"How many days {flatmate1_name} stayed in house for {bill_period} period: "))

flatmate2_name = input("What's the name of the 2nd flatmate? ")
days_in_house_flatmate2 = int(input(f"How many days {flatmate2_name} stayed in house for {bill_period} period: "))


the_bill = Bill(amount=bill_amount, period=bill_period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=days_in_house_flatmate1)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=days_in_house_flatmate2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
