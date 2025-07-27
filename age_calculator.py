def calculator_minutes(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60


    total_days = age_years * DAYS_IN_YEAR
    total_hour = total_days *HOURS_IN_DAY
    total_minute = total_hour *MINUTES_IN_HOUR

    return round(total_days),round(total_hour),round(total_minute)

while True:
    try:
        age = float(input("Enter Your age in year:  "))
        days, hours, minutes =calculator_minutes(age)

        print("\n You are approx: ")
        print(f" -  {days} days old ")
        print(f" -  {hours} Hours old ")
        print(f" -  {minutes} minutes old ")

        again = input("would You Like To Try again ? (y/n)").strip().lower()
         
        if again != "y":
            print("Good Bye ")
            break
    except:
        print("Invalid Input , Please Try Again ")

# with open("Age_calculator.txt", "a",encoding="utf-8") as f:
#     # f.write(str(age)+"\n")
#     f.write(str(age) + "\n")

# print(f"\n your Age entry ({age})has been stored  to 'Age_calculator'file.")