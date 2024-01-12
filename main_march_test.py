import main

def test_main():
    date = "March 1, 1990"
    assert main.parse_date(date) == '03/01/1990'
    