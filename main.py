
def parse_month(month):
    months={"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06", 
            "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12"}
    if month in months:
        return months[month]


def parse_date(user_string):
    x = user_string.split()
    day = str(x[1][:-1])
    month = str(parse_month(x[0]))
    year = str(x[2])
    ret = month + "/" + day + "/" + year
    return(ret)


if __name__ == '__main__':
    h=0
    while h==0:
        inp=str(input())
        if inp== "-1":
            h=1
        else:
            print(parse_date(inp))