# Leap year problem

# Function to return if year is a leap year
def LeapYear(Year):
    LeapYear = False
    # Divisible by 4 - leap year
    if Year % 4 == 0:
        LeapYear = True
        # Divisible by 100 - not a leap year
        if Year % 100 == 0:
            # Divisible by 400 - leap year
            if Year % 400 == 0:
                LeapYear = True
            else:
                LeapYear = False
        else:
            LeapYear = True
    else:
        LeapYear = False
    return LeapYear

# Main program
Year = int(input("Enter a year: "))
print(LeapYear(Year))
