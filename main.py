
def parse_date(date):
    # Split the date string into month, day, and year
    parts = date.split()
    month = parts[0]
    day = parts[1][:-1]  # Remove the comma
    year = parts[2]

    # Dictionary to map month names to their numeric representation
    months = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }

    # Format month as MM
    month = months[month]

    # Format day as DD
    if len(day) == 1:
        day = '0' + day

    # Output the date in MM/DD/YYYY format
    return month + '/' + day + '/' + year


# Main function to read and parse dates
def main():
    while True:
        date = input()
        if date == '-1':
            break
        print(parse_date(date))


if __name__ == '__main__':
    main()

#g