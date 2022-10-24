def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#write the GetHoursWorked function
def GetTotalHours():
    totalhours = input("Total hours worked: ")
    return totalhours

# write the GetHourlyRate function
def GetHourlyRate():
    hourlyrate = input("Hourly rate: ")
    return hourlyrate

# write the GetTaxRate function
def GetTaxRate():
    taxrate = input("Tax rate: ")
    return GetTaxRate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
     # write the code to print TotHours, TotGrossPay, TotTax, and TotNetpay with 2 decimal places
def printTotals(TotalHoursWorked):
    print()
    print(f"Total Hours Worked: {TotaHours}")


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
         empname = GetEmpName()
         if (empname.upper() == "END"):
              break
          # write the code to assign to hours the return value from GetHoursWorked
         totalhours = GetTotalHours()
         if (totalhours.upper() == "END"):
              break
          # write the code to assign to hourlyrate the return value GetHourlyRate
         hourlyrate = GetHourlyRate()
         if (hourlyrate.upper() == "END") :
              break

          # write the code to assign to taxrate the return value from GetTaxRate
         taxrate = GetTaxRate()
         if (taxrate == "END") :
            break
grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
TotEmployees += 1
# write the code to increment the other total variables with the appropriate values

PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
print()
print(f"Total Gross Pay: {TotGrossPay}")
print()
print(f"Total Tax: {TotTax}")
print()
print(f"Total Net Pay: {TotNetPay}")







