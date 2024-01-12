import main

def test_main():
    date = "October 31, 2000"
    assert main.parse_date(date) == '10/031/2000'