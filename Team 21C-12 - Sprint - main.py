# Sprint Week Challenge
# Date
# Author - Devon Lane
# Project 3 - Python Program




'''
Option 1. Simple IPO Program.

    The Edsel Car Rental Company rents automobiles for $35.00 per day and 10 cents per kilometer travelled.
    
    Allow the user to enter the number of days the car was rented, the mileage when the car was rented, and the mileage
    when the car was returned. Add some nice headings before the input.
    
    Display the total number of kilometers travelled, the daily cost based on the number of days and the daily rate, the
    the mileage cost based on the total kilometers travelled at the mileage rate, the cost for the rental(daily cost
    plus the mileage cost), the HST(on the daily cost only) using a rate of 15% and the total rental cost. Format the
    output with the appropriate headings - each $ value should be formatted and right aligned.
'''

def SimpleIPO():

    while True:

        while True:
            # Constants
            DAY_RATE = 35.00  # Daily Rental Cost Rate
            KM_RATE = 0.10   # Charge/Km Rate
            HST = 0.15      # HST Percentage
            COMP_NAME = "The Edsel Car Rental Company"
            try:
                DaysUsed = int(input("Enter the number of days which was rented: "))
            except ValueError:  # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                break

        while True:
            try:
                StartMileage = int(input("Enter the amount of miles upon renting the vehicle: "))
            except ValueError:  # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                break

        while True:
            try:
                EndMileage = int(input("Enter the amount of miles upon returning the vehicle: "))
            except ValueError:  # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                break
                # Calculations

        TotKmTravel = EndMileage - StartMileage
        DailyCost = (DaysUsed * DAY_RATE)
        MileCost = (TotKmTravel * KM_RATE)
        TaxesPaid = (DailyCost * HST)
        TotRentCost = TaxesPaid + DailyCost + MileCost

        TotKmTravelForm = f"${TotKmTravel:,.2f}"
        TotKmTravelPad = f"{TotKmTravelForm:>12}"
        DailyCostForm = f"${DailyCost:,.2f}"
        DailyCostPad = f"{DailyCostForm:>24}"
        MileCostForm = f"${MileCost:,.2f}"
        MileCostPad = f"{MileCostForm:>22}"
        TaxesPaidForm = f"${TaxesPaid:,.2f}"
        TaxesPaidPad = f"{TaxesPaidForm:>34}"
        TotRentCostForm = f"${TotRentCost:,.2f}"
        TotRentCostPad = f"{TotRentCostForm:>10}"

        print()
        print()
        print(COMP_NAME.title())
        print("No Rust, Dust, or Fuss!! We make buying cars easy!")
        print()
        print(f"Total Kilometer's Travelled: {TotKmTravelPad}")
        print(f"Daily Rate Cost: {DailyCostPad}")
        print(f"Mileage Rate Cost: {MileCostPad}")
        print(f"Taxes: {TaxesPaidPad}")
        print(" "*31, "-" * 9)
        print(f"Total Cost for Vehicle Rental: {TotRentCostPad}")
        print()
        print("Edsel Car Rentals, Serving your Transportation Needs")
        print()
        anykey = input("Press anykey to continue...")
        break

'''
Option 2. IF and Loop Sample.

    A common program used at interviews for programming positions is the FizzBuzz problem.
    
    Create a loop to execute 100 times. For each value if the number is divisible by 5, display the word Fizz. If the
    value is divisible by 8 display the word Buzz. If the value is divisible by both 5 and 8 display the word FizzBuzz.
    Otherwise display just the number.  A sample of the output is shown:
    
    1
    2
    3
    4
    5
    6
    7
    Buzz
    :
    :
    38
    39
    FizzBuzz
    41
    :
'''

def FizzBuzz():

    while True:
        for num in range(1, 101):
            if num % 5 == 0 and num % 8 == 0:
                print('FizzBuzz')
            elif num % 5 == 0:
                print('Fizz')
            elif num % 8 == 0:
                print('Buzz')
            else:
                print(num)
                if num == 100:
                    break


        anykey = input("Press anykey to continue...")
        break

'''
Option 3. Strings and Dates.
    
    Write a program for ABC Company that allows the user to input an employee first and last name, the date they started
     with the company, their birthday, and their yearly salary. Validate as you see fit. Calculate and display each of
     the following values as described below.
     
     -  Display the employee's name with the following formats - First Last, F. Last, and Last, F.
     
     -  Create an employee number with the format XX-XXXX-XX where the first XX is the first letter of the first and 
        last name, the middle XXXX is the year they were hired, and the last XX is the month of their birthday. Make 
        sure the value is upper case.
     
     -  Find their review date as 1 year from their hire date. Use days or weeks.
     
     -  Find the number of days till their next birthday.
     
     -  Come up with a calculation using strings or dates that would be useful for the company. 
'''

def Strings_Dates():
    while True:
        import datetime

        ALLOWED_CHAR = set("ABCDEFGHIJKLMNOPQRSTUVWXYXZ abcdefghijklmnopqrstuvwxyz - . , '")
        COMP_NAME = "ABC Company"
        HST = 0.15
        CUR_DATE = datetime.datetime.now()
        DATETIME = datetime.date.today()
        while True:
            try:
                EmpFirstName = input("Enter the employee's first name: ")
            except ValueError:   # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                if EmpFirstName in ALLOWED_CHAR == False:
                    print("Invalid Entry - Can only contain allowed alphabetical characters, ., -, '. Please re-enter.")
                else:
                    break

        while True:
            try:
                EmpLastName = input("Enter the employee's last name: ")
            except ValueError:
                print("Invalid - Must enter something.")
            else:
                if EmpLastName in ALLOWED_CHAR == False:
                    print("Invalid Entry - Can only contain allowed alphabetical characters, ., -, '. Please re-enter.")
                else:
                    break

        while True:
            try:
                EmpStartDate = input("Enter the date at which the employee was hired(YYYY-MM-DD): ")
                EmpStartDT = datetime.datetime.strptime(EmpStartDate, "%Y-%m-%d")
            except ValueError:   # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                break

        while True:
            NextBirthDTYear = 0
            try:
                EmpBirthDate = input("Enter the date of birth of the employee(YYYY-MM-DD): ")
                EmpDOB = datetime.datetime.strptime(EmpBirthDate, "%Y-%m-%d")
            except ValueError:   # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                if CUR_DATE.month == EmpDOB.month and CUR_DATE.day >= EmpDOB.day:
                    print("Invalid Entry - Birthday Cannot be in the present..")
                elif CUR_DATE.month > EmpDOB.month:
                    NextBirthDTYear = CUR_DATE.year + 1
                    break
                else:
                    break

        while True:
            try:
                EmpYearlySal = float(input("Enter the yearly salary the employee receives: "))
            except ValueError:  # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                break

        # Calculations

        NextBirthday = datetime.date(NextBirthDTYear, EmpDOB.month, EmpDOB.day)
        NumDaysTilBday = (NextBirthday - DATETIME).days
        ReviewDate = EmpStartDT + datetime.timedelta(days=365)
        ReviewDays = (ReviewDate - CUR_DATE).days
        BenefitDate = EmpStartDT + datetime.timedelta(days=120)
        BenefitDT = datetime.datetime.strftime(BenefitDate, "%B %d, %Y")
        NumSickDays = ((EmpStartDT - CUR_DATE) // datetime.timedelta(days=28)) * -1.5
        TaxesHeld = EmpYearlySal * HST
        NetPay = EmpYearlySal - TaxesHeld

        print(COMP_NAME.title())
        print()
        print()
        print(f"Employee can be referred to as: {EmpFirstName}{EmpLastName}, {EmpFirstName[0]}. {EmpLastName}, and "
              f"{EmpLastName}, {EmpFirstName[0]}")
        print()
        print(f"Employee ID No.:                {EmpFirstName[0]}{EmpLastName[0]}-{EmpStartDate[0:4]}-{EmpBirthDate[5:7]}")
        print(f"Employee Review Date:           {ReviewDays} Days")
        print(f"Number of days till birthday:   {NumDaysTilBday} Days")
        print(f"Benefits start date:            {BenefitDT}")
        print(f"Sick Days Accumulated:          {NumSickDays} Days")
        print()
        print(f"Gross Pay:                      ${EmpYearlySal:,.2f}")
        print(f"Taxes:                          ${TaxesHeld:,.2f}")
        print(" " * 31, "-" * 8)
        print(f"Net Pay:                        ${NetPay:,.2f}")
        print()
        anykey = input("Enter anykey to continue...")
        break

'''
Option 4. Data files and Default Values.

    Using the Edsel Car Rental Company program, copy the program from Option 1 and add the following to the program.
    
     -  Add a loop to repeat the program until the user enters a 0(Zero) for the number of days rented.
     
     -  Create a defaults file called ECRDef.dat. The file contains the next rental number, the daily rental rate, the 
        mileage rate, and the HST rate.
        
       1438
       35.00
       0.10
       0.15
       
       Read the values from the defaults file at the beginning of the function and write the current values back at the
       end of the program.
    
     -  After the output, add a section of code that will write the rental number, the input values, and all the 
        calculated values to a file called Rentals.dat. Display a message for the user indicating that the rental
        information has been saved. Add 1 to the rental number.
'''

def DataFiles_DefaultValues():



    f = open('ECRDef.dat', 'r')
    RENTAL_NUM = int(f.readline())
    DAY_RATE = float(f.readline())
    KM_RATE = float(f.readline())
    HST = float(f.readline())
    f.close()

    # Constants
    COMP_NAME = "The Edsel Car Rental Company"
    DAY_RATE = 35.00
    KM_RATE = 0.10
    HST = 0.15
    while True:
        StartMileage = 0
        EndMileage = 0
        try:
            DaysUsed = int(input("Enter the number of days which was rented(Enter 0 to exit): "))
        except ValueError:  # Ensures a value was entered
            print("Invalid - Must enter something.")
        else:
            if DaysUsed == 0:
                break

            StartMileage = int(input("Enter the amount of miles upon renting the vehicle: "))
            EndMileage = int(input("Enter the amount of miles upon returning the vehicle: "))
            print()

            # Calculations

            TotKmTravel = EndMileage - StartMileage
            DailyCost = (DaysUsed * DAY_RATE)
            MileCost = (TotKmTravel * KM_RATE)
            TaxesPaid = (DailyCost * HST)
            TotRentCost = TaxesPaid + DailyCost + MileCost


            TotKmTravelForm = f"{TotKmTravel}km"
            TotKmTravelFormStr = str(TotKmTravelForm)
            TotKmTravelPad = f"{TotKmTravelForm:>12}"
            DailyCostForm = f"${DailyCost:,.2f}"
            DailyCostFormStr = str(DailyCostForm)
            DailyCostPad = f"{DailyCostForm:>24}"
            MileCostForm = f"${MileCost:,.2f}"
            MileCostFormStr = str(MileCostForm)
            MileCostPad = f"{MileCostForm:>22}"
            TaxesPaidForm = f"${TaxesPaid:,.2f}"
            TaxesPaidFormStr = str(TaxesPaidForm)
            TaxesPaidPad = f"{TaxesPaidForm:>34}"
            TotRentCostForm = f"${TotRentCost:,.2f}"
            TotRentCostFormStr = str(TotRentCostForm)
            TotRentCostPad = f"{TotRentCostForm:>10}"

            print(COMP_NAME.title())
            print("No Rust, Dust, or Fuss!! We make buying cars easy!")
            print()
            print(f"Total Kilometer's Travelled: {TotKmTravelPad}")
            print(f"Daily Rate Cost: {DailyCostPad}")
            print(f"Mileage Rate Cost: {MileCostPad}")
            print(f"Taxes: {TaxesPaidPad}")
            print(" " * 31, "-" * 9)
            print(f"Total Cost for Vehicle Rental: {TotRentCostPad}")
            print()
            print("Edsel Car Rentals, Serving your Transportation Needs")
            print()



            RENTAL_NUM += 1

            f = open('ECRDef.dat', "a")  # "a" adds to the end, "w" overwrites.
            f.write(f"Rental Number: {RENTAL_NUM}, ")
            f.write(f"Daily Rate: {DailyCostFormStr}, ")
            f.write(f"Milage Rate: {MileCostFormStr}, ")
            f.write(f"Total Km Travelled: {TotKmTravelFormStr}, ")
            f.write(f"Total Rental Cost: {TotRentCostFormStr}, ")
            f.write(f"HST: {TaxesPaidFormStr},\n ")
            f.close()


            print("Saving...", end='')
            for wait in range(1, 10):
                print('*', end='')


            print()
            print("Vehicle Rental Information for {} successfully saved.".format(RENTAL_NUM))
            Anykey = input("Press any key to continue...")

            f = open('Def.dat', 'w')
            f.write("{}\n".format(str(RENTAL_NUM)))
            f.write("{}\n".format(str(DAY_RATE)))
            f.write("{}\n".format(str(KM_RATE)))
            f.write("{}\n".format(str(HST)))
            f.close()


def Areas():

    while True:
        Radius = 0
        PI = 3.1459265
        print()
        print("Areas of Shapes")
        print()
        print("From the list below choose:")
        print("1. Area of a Circle")
        print("2. Area of a Half Circle")
        print("3. Area of a Equilateral or Right Triangle")
        print("4. Area of a Square/Rectangle")
        print("5. Area of a Trapezoid")
        print("6. Exit back to Main Menu")
        print()
        try:
            Choice = int(input("Enter a number from the list above: "))
        except ValueError:
            print("Invalid - Must enter a numerical value between 1 - 6. Use the list above for reference.")
        else:
            if Choice == 1:
                Radius = float(input("Please enter the radius of the circle(1/2 the Diameter): "))
                Area1 = (PI) * (Radius)**2
                print(f"The area of the Circe is {Area1}m^2.")
                print()
                anykey = input("Press anykey to continue..")
            elif Choice == 2:
                Radius = float(input("Please enter the radius of the circle(1/2 the Diameter): "))
                Area2 = ((PI) * (Radius)**2) // 2
                print(f"The area of the Half Circle is {Area2}m^2.")
                print()
                anykey = input("Press anykey to continue..")
            elif Choice == 3:
                Base = float(input("Please enter the length of the base of the triangle: "))
                Height = float(input("Please enter the length of the height of the triangle: "))
                Area3 = ((Base) * (Height)) // 2
                print(f"The area of the Triangle is {Area3}m^2.")
                print()
                anykey = input("Press anykey to continue..")
            elif Choice == 4:
                Base = float(input("Please enter the length of the base of the square/rectangle: "))
                Height = float(input("Please enter the length of the height of the square/rectangle: "))
                Area4 = (Base) * (Height)
                print(f"The area of the Square/Rectangle is {Area4}m^2.")
                print()
                anykey = input("Press anykey to continue..")
            elif Choice == 5:
                SmallBase = float(input("Enter the smaller base length of the Trapezoid: "))
                LargeBase = float(input("Enter the larger length of the base of the Trapezoid: "))
                Height = float(input("Enter the height of the Trapezoid: "))
                Area5 = ((SmallBase + LargeBase)/2) * Height
                print(f"The are of the Trapezoid is {Area5}.")
                print()
                anykey = input("Press anykey to continue..")
            elif Choice == 6:
                break

def RoomForError():

    while True:
        import math

        Num1 = 0
        Num2 = 0
        while True:
            try:
                Num1 = float(input("Enter a positive number: "))

            except ValueError:   # Ensures a value was entered
                print("Invalid - Must enter something.")
            else:
                if Num1 < 0:
                    print("Invalid Entry - Must enter a positive number.")
                else:
                    break
        while True:
            try:
                Num2 = float(input("Enter a negative number: "))
            except ValueError:  # Ensures a value was entered
                print("Invalid Entry - Must enter a negative number.")
            else:
                if Num2 > 0:
                    print("Invalid Entry - Must enter a negative number.")
                else:
                    break
        print(math.erf(Num1))
        print(math.erf(Num2))
        anykey = input("Press anykey to continue..")
        break
'''
Prepare the following program. The menu identifies different options you are to prepare using functions. Create at least
2 other functions in the program that include parameters and return values.

    The Sprint Project Company

    1. Simple IPO Program
    2. IF and Loop Sample
    3. Strings and Dates.
    4. Data files and Default Values.
    5. Areas
    6. Error Function
    8. Quit

        Enter choice(1-5).
'''

while True:


    while True:
        print()
        print("Project #3 - Main Menu")
        print()
        print("1. Simple IPO.")
        print("2. FizzBuzz.")
        print("3. Strings and Dates.")
        print("4. Data files and Default Values.")
        print("5. Areas.")
        print("6. RoomForError.")
        print("7. Quit.")
        print()
        try:
            Choice = int(input("Choose a number between 1 - 8: "))
        except ValueError:  # Ensures a value was entered
            print("Invalid Entry - Must be a number between 1 - 8: ")
        else:
            if Choice == 1:
                SimpleIPO()
            elif Choice == 2:
                FizzBuzz()
            elif Choice == 3:
                Strings_Dates()
            elif Choice == 4:
                DataFiles_DefaultValues()
            elif Choice == 5:
                Areas()
            elif Choice == 6:
                RoomForError()
            elif Choice == 7:
                exit()
