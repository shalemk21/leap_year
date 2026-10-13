import sys
def is_leap_year(year):
    """Check if a year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python leap_year.py <year>")
        sys.exit(1)
    try:
        year = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the year.")
        sys.exit(1)
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")