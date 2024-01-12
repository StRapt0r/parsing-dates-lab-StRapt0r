import main

def test_main():
    date = "May 5, 2010"
    assert main.parse_date(date) == '05/05/2010'