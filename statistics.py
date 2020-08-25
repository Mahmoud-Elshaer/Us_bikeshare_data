import time
import pandas as pd
import numpy as np

 
#definition of most common month function
def common_month(df):
    df['month'] = df['Start Time'].dt.month_name()
    popular_month=df['month'].mode()[0]
    print('Most Popular Start Month:',popular_month)
#definition of most common day function
def common_day(df):
    df['day'] = df['Start Time'].dt.day_name()
    popular_day=df['day'].mode()[0]
    print('Most Popular Day:',popular_day)
#definition of most common start hour function
def common_start_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Popular Start Hour:',popular_hour)

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour

    if(month=='all' and day=='all'):
        # display the most common month
        common_month(df)
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_start_hour(df)
    elif(month!='all' and day=='all'):
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_start_hour(df)
    elif(month=='all' and day!='all'):
        # display the most common start hour
        common_start_hour(df)
        # display the most common month
        common_month(df)
    elif(month!='all'and day!='all'):
        common_start_hour(df)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station:',popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station:',popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    popular_start_end = df['combination'].mode()[0]    
    print("The most frequent combination of start station and end station trip is: ", popular_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type:\n',user_types)
    
    if city=='new york city' or city=='chicago':
        
        # TO DO: Display counts of gender
        gender_types = df['Gender'].value_counts()
        print('Gender Type:\n',gender_types)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = int(df['Birth Year'].min())
        print('Earliest Year Birth: ',earliest_year_birth)
        most_recent_year_birth =int(df['Birth Year'].max())
        print('Most Recent Year Birth: ',most_recent_year_birth)
        most_common_year_birth = int(df['Birth Year'].mode()[0])
        print('Most common Year Birth: ',most_common_year_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


