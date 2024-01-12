import main

def test_main():
    date = "January 1, 2000"
    assert main.parse_date(date) == '01/01/2000'