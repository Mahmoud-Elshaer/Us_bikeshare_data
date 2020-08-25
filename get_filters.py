import time
import pandas as pd
import numpy as np


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('To view the available bikeshare data, type:\n (a) for '
                         'Chicago\n (b) for New York City\n (c) for Washington\n ').lower()
            if city in ['a','b','c']:
                if city == "a":
                    city = 'chicago'
                elif city == 'b':
                    city = 'new york city'
                else:
                    city =  'washington'
                print("Your choice is {}".format(city))
                # Terminate the loop once getting a right answer
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid city choice!!')
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            answer = input('\n\n Would you like to filter {}\'s data by month, day, or not at'
                          ' all? type\n (m) for month\n (d) for day\n (none) for not at all \n'.format(city.title())).lower()
            if answer in ['m','d','none']:
                if answer == "m":
                    while True:
                        try:
                            month_in = input('\n please choose a month\n'
                                          '(Jan) for January\n'
                                          '(Feb) for February\n'
                                          '(Mar) for March\n'
                                          '(Apr) for April\n'
                                          '(May) for May\n'
                                          '(Jun) for June\n').lower()
                            months = {'jan':'January','feb':'February','mar':'March','apr':'April','may':'May','jun':'June'}
                            #print(months[month_in])
                            if month_in in months:
                                month = months[month_in]
                            # Terminate the loop once getting a right answer
                            break
                        except KeyboardInterrupt:
                            print('\nNO Input Taken!')
                        else:
                            print('Invalid month choice!!')
                    answer = month
                    day = 'all'
                elif answer == 'd':
                    while True:
                        try:
                            # get user input for day of week (all, monday, tuesday, ... sunday)
                            week_day = input('\n please choose a day\n'
                                          '(Mon) for Monday\n'
                                          '(Tue) for Tuesday\n'
                                          '(Wed) for Wednesday\n'
                                          '(Thu) for Thursday\n'
                                          '(Fri) for Friday\n'
                                          '(Sat) for Saturday\n'
                                          '(Sun) for Sunday\n').lower()
                            week_days ={'mon':'Monday',
                                        'tue':'Tuesday',
                                        'thu':'Thursday',
                                        'fri':'Friday',
                                        'sat':'Saturday',
                                        'sun':'Sunday'}
                            if week_day in week_days:
                                day = week_days[week_day]
                            break
                        except KeyboardInterrupt:
                            print('\nNO Input Taken!')
                        else:
                            print('Invalid day choice!!')

                    answer = day
                    month = 'all'
                else:
                    answer =  'none'
                    month= 'all'
                    day = 'all'
                print("Your choice is {}".format(answer))
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid city choice!!')

    print('-'*40)

    return city, month, day
