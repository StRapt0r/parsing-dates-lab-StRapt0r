import main

def test_main():
    date = "September 2, 2024"
    assert main.parse_date(date) == '09/02/2024'