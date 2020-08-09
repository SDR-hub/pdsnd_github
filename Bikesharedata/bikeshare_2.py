import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# List the months and days values
months= ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all'] 
cities=['chicago', 'new york', 'whashington', 'all']

    
def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Welcome! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington)


while True:
    city = input("What city would you like data for? (Chicago, New York City, Washington)\n--> ").lower()
    if city not in cities:
       print(' Oops. Please type a valid city: Chicago, New York City, or Washington.')
       continue
    else:
       break

# TO DO: get user input for month (all, january, february, ... , june)
while True:
    month =  input("Please enter the name of the month (Jan to June or all) to analyze: For all months type 'all'\n--> ").lower()
    if month.lower() not in months:
       print(' Oops. Please type a valid month: January to June')
       continue
    if month != 'all':
       month_name=['january','february','march','april','may','june']
       month= month_name.index(month)+ 1
       df=df[df['month'] == month]
    else:
       break
    

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
while True:
    day = input("Please enter the day of the week or all to analyze:\n-->").lower()
    if day not in days:
        print('Oops. Please type a valid day of the week: Monday to Sunday or all ')
        continue
    if day != 'all':
       day_name=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
       day= day_name.index(day)+ 1
       df=df[df['day'] == day]
    else:
        break
      

print('-'*40) 
    
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
df=pd.read_csv(CITY_DATA[city])
   
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()

# Converts the Start Time column to date time.
df['Start Time']= pd.to_datetime(df['Start Time'])

# TO DO: display the most common month
df['month']= df['Start Time'].dt.month
common_month = df['month'].mode()[0]
print("The most common month of travel was {}.\n".format(common_month))


# TO DO: display the most common day of week
df['day']= df['Start Time'].dt.weekday_name
common_day = df['day'].mode()[0]
print("The most common day of travel was {}.\n".format(common_day))


# Extract the hour from Start Time and create an hour column. 
df['hour']= df['Start Time'].dt.hour

# TO DO: Display the most common start hour
common_start_hour = df['hour'].mode()[0]
print("Most common start hour of travel is at {}.\n".format(common_start_hour))
print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()

# TO DO: display most commonly used start station
common_start = df['Start Station'].mode()[0]
print("The most commonly used starting station was {}.\n".format(common_start))

# TO DO: display most commonly used end station
common_end = df['End Station'].mode()[0]
print("The most commonly used ending station was {}.\n".format(common_end))

# TO DO: display most frequent combination of start station and end station trip
stations_combined = df.groupby(['Start Station','End Station']).size().nlargest(1)
print("The most frequently used start and end stations were {}.\n".format(stations_combined))

print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

print('\nCalculating Trip Duration...\n')

# TO DO: display total travel time
total_travel = df['Trip Duration'].sum()
print ('\nTotal travel time:', total_travel)

# TO DO: display mean travel time
mean_travel = df['Trip Duration'].mean()
print('\nMean travel time:', mean_travel)

print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
print('\nCalculating User Stats...\n')

# TO DO: Display counts of user types
if 'User Type' in df.columns:
    user_types = df['User Type'].value_counts()
    print("The user types are: {}\n".format(user_types))
    
# TO DO: Display counts of gender
gender_counts = df['Gender'].value_counts()
print("The gender counts (available only for New York and Chicago)are: {}\n".format(gender_counts))

# TO DO: Display earliest, most recent, and most common year of birth
print ('Birth Year Data available only for New York and Chicago')

earliest = min(df['Birth Year'])
most_recent = max(df['Birth Year'])
most_common = df['Birth Year'].mode()[0]
print("The earliest year of birth was {}.\n".format(earliest))
print("The most recent year of birth was {}.\n".format(most_recent))
print("The most common year of birth was {}.\n".format(most_common))

  
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
i = 0
while True:
  display_more=input("Do you want to see 5 more lines of data? Yes or No.\n").lower()
  if display_more=='yes':
    five_rows=df.iloc[:i+5]
    print(five_rows)
    i+= 5
  else:
    break


   
def main():
    city, month, day = get_filters(city, month, day)
    df = load_data(city, month, day)
        
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    
restart = input('\nWould you like to restart? Enter yes or no.\n')
while restart=='yes':
    f = open("bikeshare.py")
    exec(f.read())
    
    if restart.lower() != 'no':
        break
    if __name__ == "__main__":
	    main()
    

