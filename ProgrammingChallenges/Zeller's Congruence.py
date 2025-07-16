#Zeller's Congruence finds day of week given a date
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]

try:
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))

    assert month in range(1,13)
    assert day in range(1,days_in_months[month]+1)
    
    
except:
    print("Incorrect input")
    quit()
    

if month<= 2:
    month+= 10
    year -=1
else:
    month -=2


month_correction = (26*month -2)//10

century = year//100

century_remainder = year%100

year_correction = century *5 +century_remainder + century_remainder//4 + century/4




weekDay = (day+ month_correction + year_correction)%7
daysOfTheWeek = {0: 'Sunday', 1:'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: "Thursday", 5: "Friday", 6:"Saturday"}
print(daysOfTheWeek[weekDay])
