import random

def main():
    
    month = input("Enter  month: ")
    salary = float(input("Enter salary of the month: "))
    savings_percentage = float(input("Enter percentage for savings: "))
    rent_percentage = float(input("Enter percentage for rent: "))
    electricity_percentage = float(input("Enter percentage for electricity: "))
    
    
    savings_amount = (savings_percentage / 100) * salary
    rent_amount = (rent_percentage / 100) * salary
    electricity_amount = (electricity_percentage / 100) * salary
    
    total_expenses = savings_amount + rent_amount + electricity_amount
    remainder = salary - total_expenses
    
    yearly_rent = rent_amount * 12
    yearly_electricity = electricity_amount * 12
    
    salary_squared = salary ** 2
    
    additional_savings = random.randint(20, 100)  
    leftover_after_additional_savings = additional_savings / savings_amount if savings_amount > 0 else 0
    
    
    print(f"Salary: ${salary:.2f}")
    print(f"Savings : ${savings_amount:.2f}")
    print(f"Rent : ${rent_amount:.2f}")
    print(f"Electricity : ${electricity_amount:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Salary: ${remainder:.2f}")
    print(f"Estimated Yearly Rent: ${yearly_rent:.2f}")
    print(f"Estimated Yearly Electricity Cost: ${yearly_electricity:.2f}")
    print(f"Salary Squared (for fun!): {salary_squared:.2f}")
    print(f"Leftover when additional ${additional_savings} is divided by savings: {leftover_after_additional_savings:.2f}")
   

if __name__ == "__main__":
    main()
