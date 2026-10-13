import sys


def is_leap_year(year: int) -> str:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "is leap year"
    return "is not leap year"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
        print(f"{year} {is_leap_year(year)}.")