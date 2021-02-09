import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    while True :
        print('please chose a city: chicago, new york city or washington')
        city = input().lower()
        if city not in CITY_DATA.keys():
            print('please enter correct input choose city: chicago, new york city or washington ')
        else:
            break
        
   
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january' : 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    while True :
        print('please chose month: january, february, march, april, may, june or all')
        month = input().lower()
        if month not in MONTH_DATA.keys():
            print('please enter correct input choose month: january, february, march, april, may, june or all ')
        else:
            break
     
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
   
    while True:
        print('please choose a day: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ')
        day = input().lower()
        if day not in day_list :
            print('please inter correct input choose a day: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all')
        else :
     
            break
    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month by using mode method
    common_month = df['month'].mode()[0]
    print(f'The most common month is : {common_month}')
  
    # TO DO: display the most common day of week by using mode method
    common_day = df['day_of_week'].mode()[0]
    print(f'The most common day is : {common_day}')      

    # TO DO: display the most common start hour by using mode method
    #firt i should extract the hour from start time and create hour colomn      
    df['hour'] = df['Start Time'].dt.hour
    common_hour= df['hour'].mode()[0]   
    print(f'The most common start hour is : {common_hour}')    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station by using mode method
    commonly_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is : {commonly_start_station}')    
          


    # TO DO: display most commonly used end station by using mode metod 
    commonly_end_station= df['End Station'].mode()[0]
    print(f'The most commonly used End station is : {commonly_end_station}') 


     #TO DO: display most frequent combination of start station and end station trip
    
    group= df.groupby(['Start Station' , 'End Station'])
    common_combination_station= group.size().sort_values(ascending=False).head(1)
    print(f'The most frequent combination of Start station and End station : \n {common_combination_station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time by using Sum method 
    total_travil_time = df['Trip Duration'].sum()
    print(f'The total travel time : {total_travil_time}') 
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'The mean travel time : {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types by using value_counts method
    user_types = df['User Type'].value_counts()
    print(f'User type stats : {user_types}')

    # TO DO: Display counts of gender
    # if cluse because in washington file not have gender colomn 
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print(f'Gender stats : {gender}')
        

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year= int(df['Birth Year'].min())
        recent_year= int(df['Birth Year'].max())
        common_year= int(df['Birth Year'].mode()[0])
        
        print(f'The earliest year of birht :  {earliest_year}\nThe most recent year of birth : {recent_year} \nThe most common year of birth : {common_year} ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def display_raw(df):
    respose_list= ['yes','no']
    raw_data=''
    counter=0
    while raw_data not in respose_list:
        print('Do you want to view the raw data? yes or no ?')
        raw_data= input().lower()
        if raw_data=='yes':
            print (df.head())
        elif raw_data not in respose_list:
            print ('please check your input ')
    while raw_data=='yes':
        print('Do you want to view more raw data? yes or no ?')
        counter=counter+5
        raw_data=input().lower()
        if raw_data=='yes':
            print (df[counter:counter+5])
        elif raw_data !='yes':
            break
    print('-'*40)
        
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw(df)

        restart = input('\n Would you like to restart? Enter yes or no ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
