Basic Data Exploration with pandas on Bikeshare Data

This project focuses on pandas library usage and simple statistics methods to perform descriptive analysis on the bikeshare data from three major U.S. cities - Chicago, Washington, and New York City - to display information such as most popular days or most common stations.

Running the program
You can input 'python bikeshare.py' on your terminal to run this program. 

Program Details
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:

Most popular MONTH
Most popular DAY
Most popular HOUR
Most popular START station
Most popular END station
Most popular combination of start and end stations
Total trip DURATION
Average trip duration
Types of users by number
Types of users by gender (if available)
The oldest user (if available)
The youngest user (if available)
The most common birth year amongst users (if available)
Finally, the user is prompted with the choice of restarting the program or not.

Requirements

Language: Python 3.6 or above
Libraries: pandas, numpy, time

Project Data

chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.
new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.
washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.
