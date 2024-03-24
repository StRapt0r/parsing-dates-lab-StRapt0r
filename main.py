#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    months={"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06",
            "July":"07","August":"08","September":"09","October":"10","November":"11","December":"12",}
    for i in months:
        if month==months[i]:
            return(months[i])

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    x = x.split(user_string)
    for i in x:
        x[i].replace(" ", "")
        x[i].replace(",", "")
    x[0]=parse_month(x[0])
    for i in range(2):
        x[i].append("/")
    x=(str(y) for y in x)
    return(x)

#March 1, 1990
#03/01/1990
#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    h=0
    while h==0:
        inp=input()
        if inp== -1 or "-1":
            h=1
        else:
            print(parse_date(inp))