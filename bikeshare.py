import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("\nWhich city would you like to analyze? (Chicago, New York City, Washington)\n").strip().lower()
        if city in cities:
            break
        else:
            print("\nPlease enter a valid city name.")

    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'none']
        month = input("\nWhich month would you like to consider? (January, February, March, April, May, June)? Type 'None' for no month filter\n").strip().lower()
        if month in months:
            break
        else:
            print("\nPlease enter a valid month.")

    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'none']
        day = input("\nWhich day of the week would you like to consider? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'None' for no day filter\n").strip().lower()
        if day in days:
            break
        else:
            print("\nPlease enter a valid day.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'none':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df, month, day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if month == 'none':
        pop_month = df['month'].mode()[0]
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        pop_month = months[pop_month - 1]
        print("The most popular month is", pop_month)

    if day == 'none':
        pop_day = df['day_of_week'].mode()[0]
        print("The most popular day is", pop_day.title())

    df['Start Hour'] = df['Start Time'].dt.hour
    pop_hour = df['Start Hour'].mode()[0]
    print("The most popular start hour is {}:00 hrs".format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    pop_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}".format(pop_start_station))

    pop_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is {}".format(pop_end_station))

    df['combination'] = df['Start Station'] + " to " + df['End Station']
    pop_com = df['combination'].mode()[0]
    print("The most frequent combination of start and end station is {} ".format(pop_com))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hour, minute, second))

    average_duration = round(df['Trip Duration'].mean())
    m, sec = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print("The average trip duration: {} hour(s) {} minute(s) {} second(s)".format(h, m, sec))
    else:
        print("The average trip duration: {} minute(s) {} second(s)".format(m, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df, city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_counts = df['User Type'].value_counts().to_dict()
    print("The user types are:\n", user_counts)

    if city in ['chicago', 'new york city']:
        gender_counts = df['Gender'].value_counts().to_dict()
        print("\nThe counts of each gender are:\n", gender_counts)

        earliest = int(df['Birth Year'].min())
        print("\nThe oldest user is born in the year", earliest)
        most_recent = int(df['Birth Year'].max())
        print("The youngest user is born in the year", most_recent)
        common = int(df['Birth Year'].mode()[0])
        print("Most users are born in the year", common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
