import main

def test_main():
    date = "December 13, 2003"
    assert main.parse_date(date) == '12/13/2003'