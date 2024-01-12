import main

def test_main():
    date = "November 15, 2005"
    assert main.parse_date(date) == '11/15/2005'