
class ROI_Calc():

    def income(self):
        rent_income = input("How much does this property rent for? $")
        misc_income = input("How much additional income does this property provide? $")
        month_income = float(rent_income) + float(misc_income)
        self.monthly_income = "{:.2f}".format(month_income)
        print(f"\nThe total monthly income for this property is ${self.monthly_income}.\n")


    def expenses(self):
        tax = input("How much monthly tax is owed for for this property? ")
        insurance = input("What is the monthly cost of insurance for this property? ")
        utilities = ""
        utilities_q = input("Is the tenant responsible for paying the utility bills? (Y/N) ")
        if utilities_q.lower() == "y":
            utilities = 0
        else:
            electric = input("What is the average monthly electric bill for this property? $")
            water = input("What is the average monthly water bill for this property? $")
            sewer = input("What is the average monthly sewer bill for this property? $")
            garbage = input("What is the average monthly garbage bill for this property? $")
            gas = input("What is the average monthly gas bill for this property? $")
            utilities = float(electric) + float(water) + float(sewer) + float(garbage) + float(gas)
        hoa = input("What are the monthly HOA fees for this property? $")
        maintenance = input("What is the monthly cost of maintenance for this property? $")
        vacancy = input("How much money do you set aside each month to prepare for future property vacancy? $")
        repairs = input("How much money do you set aside each month for future repairs of the property? $")
        capex = input("How much money do you spend each month for capital expenditures? (repairs, renovations, etc.) $")
        prop_man = input("How much money do you spend on property management each month for this property? $")
        mortgage = input("What is the monthly mortgage payment on this property? $")
        month_expenses = float(tax) + float(insurance) + float(utilities) + float(hoa) + float(maintenance) + float(vacancy) + float(repairs) + float(capex) + float(prop_man) + float(mortgage)
        self.monthly_expenses = "{:.2f}".format(month_expenses)
        print(f"\nThe total monthly expenses for this property are ${self.monthly_expenses}.\n")

    
    def cashflow(self):
        month_cashflow = float(self.monthly_income) - float(self.monthly_expenses)
        self.monthly_cashflow = "{:.2f}".format(month_cashflow)
        print(f"\nThe monthly cash flow for this property is ${self.monthly_cashflow}.\n")

    def annual_ROI(self):
        down_p = input("What was your total down payment on this property? $")
        closing_c = input("How much were your closing costs on this property? $")
        reno = input("How much did you spend renovating this property? ")
        misc = input("What other one-time expenses have you spent on this property? ")
        total_investment = float(down_p) + float(closing_c) + float(reno) + float(misc)
        yearly_cashflow = float(self.monthly_cashflow) * 12
        roi = yearly_cashflow / total_investment * 100
        self.roi_percent = round(roi, 2)

        print(f"\nMonthly Income: ${self.monthly_income}")
        print(f"Monthly Expenses: ${self.monthly_expenses}")
        print(f"Monthly Cash Flow: ${self.monthly_cashflow}")
        print(f"\nANNUAL ROI: {self.roi_percent}%")


property1 = ROI_Calc()

def run():
    while True:
        property1.income()
        property1.expenses()
        property1.cashflow()
        property1.annual_ROI()
        break
run()
