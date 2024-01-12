import main

def test_main():
    date = "June 10, 2013"
    assert main.parse_date(date) == '06/10/2013'