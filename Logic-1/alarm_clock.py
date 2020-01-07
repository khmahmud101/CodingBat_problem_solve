def alarm_clock(day, vacation):
    if (day == 0 or day == 6) and vacation is True:
        return 'off'
    elif (day == 1 or day == 2 or day == 3 or day == 4 or day == 5) and vacation == True:
        return '10:00'
    elif (day == 0 or day == 6) and vacation == False:
        return '10:00'
    else:
        return '7:00'
