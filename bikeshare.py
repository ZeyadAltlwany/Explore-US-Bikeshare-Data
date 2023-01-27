#!/usr/bin/env python
# coding: utf-8
import time
import pandas as pd
import numpy as np




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['January','February','March','April','May','June','All']
Days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']





def get_month():
    while True :
        month = input('please enter the month you want to filter with if you want all year enter "all" \n [January,February,March,April,May,June,All] :\n').capitalize()
        if month in months :
            month=(months.index(month)+1)
            break
        
        else:
            print('please enter a month correctly')
    return month

def get_city():
     while True :
        city =input('Would you like to see data for chicago, new york city, or washington ? \n')
        city=city.lower()
        if CITY_DATA.get(city) !=None :
            return city
        else:
            continue
     
def get_day():
    days=['M', 'T', 'W', 'T', 'F','S', 'S','All']

    while True :
        day = input('please enter the day you want to filter with  [M, T, W, T, F,S, S, All] if you want all year enter "all"\n')
        day=day.capitalize()
        if day in days :
            day=days.index(day)
            return day
        else:
            print('please enter a day correct')



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    city =get_city()
    month =get_month()
    day=get_day()


    print('-'*40)
    return city, month, day





def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']= df['Start Time'].dt.month[:]
    df['wday'] = df['Start Time'].dt.dayofweek
    if day != 7 :
        df = df[df['wday'] ==day]
        
    if month !=7:
        df = df[df['month'] ==month]

    return df




def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    if month==7:
     
      counta =df['month'].value_counts()[popular_month]
      print('Most Popular month : {}'.format(popular_month) )
      print('counts  : {} \n'.format( counta))
    else:
      counta =df['month'].value_counts()[popular_month]
      print('total rides in {} is  : {} \n'.format( months[(month-1)],counta))

    # display the most common day of week
   
    if month==7:
        popular_day = df['wday'].mode()[0]
        counta =df['wday'].value_counts()[popular_day]
        print('Most Popular day : {}'.format(popular_day) )
        print('counts  : {} \n'.format( counta))

    else:
      print('total rides in {} in your timerange is  : {} \n'.format( Days[(day)],counta))
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    counta =df['hour'].value_counts()[popular_hour]
    print('Most Popular Start Hour : {} '.format(popular_hour))
    print('total rides in this hour in your timerange is  : {} \n'.format( counta))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_sstation = df['Start Station'].mode()[0]
    counta = df['Start Station'].value_counts()[popular_sstation]
    print('most common Start station in your timerange is :{}'.format(popular_sstation))
    print('with count : {}'.format(counta))

    # display most commonly used end station
    popular_estation = df['End Station'].mode()[0]
    counta = df['End Station'].value_counts()[popular_estation]
    print('most common End station in your timerange is :{}'.format(popular_estation))
    print('with count : {}'.format(counta))
    # display most frequent combination of start station and end station trip
    df['SE']=df['Start Station']+'  -  '+df['End Station']
    popular = df['SE'].mode()[0]
    counta = df['SE'].value_counts()[popular]
    print('most frequent combination of start station and end station trip :{}'.format(popular))
    print('with count : {}'.format(counta))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['traveltime'] = (df['End Time']-df['Start Time']).dt.total_seconds()
    sum =(df['traveltime'].sum())/60
    print('total travel time is {} minutes'.format(sum))
    # display mean travel time
    avg=(df['traveltime'].mean())/60
    print('mean travel time : {} minutes'.format(avg))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # Display counts of gender
    user_gender = df['Gender'].value_counts()
    print('\n')
    print(user_gender)
    # Display earliest, most recent, and most common year of birth
    earliest=df['Birth Year'].min()
    print ('\noldest user birthyear is {}'.format(int(earliest)))

    young=df['Birth Year'].max()
    print ('youngest user birthyear is {}'.format(int(young)))
    
    avg=df['Birth Year'].mean()
    print ('average birthyear is {}'.format(int(avg)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_row(df):
    temp=0
   
    while True :
        i = input ('would you see more rows about data ? (yse/ no)')
        i=i.lower()
        if i=='yes'  :
           print( df[temp:temp+5])
           temp+=5
        elif i =='no' :
            break
        else :
            print('please choose (yes/no)')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        if city =='chicago' or city=='new york city':
            user_stats(df)
        get_row(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()


