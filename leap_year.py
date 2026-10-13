import sys
def is_leap_year(year):
   
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
if __name__ == "__main__":
    year = int(sys.argv[1])
    is_leap_year(year)