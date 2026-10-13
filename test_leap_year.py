from leap_year import is_leap_year


def test_is_leap_year():
    assert is_leap_year(2028) == "is leap year"


def test_is_no_leap_year():
    assert is_leap_year(2027) == "is not leap year"