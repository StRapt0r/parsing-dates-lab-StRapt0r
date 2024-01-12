import main

def test_main():
    date = "July 4, 1776"
    assert main.parse_date(date) == '07/04/1776'