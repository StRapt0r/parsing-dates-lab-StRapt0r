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
    bannana=user_string.split()
    x=0
    retdate=""
    for i in bannana:
        x+=1
        if x==1:
            month=parse_month(i)
        elif x==2:
            i=i.replace(",","")
            i=i.replace(" ","")
            if len(i) < 2:
                i="0"+i
            day=i
        elif x==3:
            i=i.replace(" ","")
            year=i
    return(str(month) + "/" str(day) + "/" str(year))

#March 1, 1990
#03/01/1990
#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    data=[]
    z=input()
    while -1 != z:
        data.append(z)
        z=input()
    for y in data:
        print(parse_date(y))