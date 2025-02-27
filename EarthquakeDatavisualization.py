'''
Program: Nuclear Explosion,Rock Burst,Explosion,Earthquake Data visualization
Author: Prashanth Reddy Loka
Description: This Python script analyzes earthquake data to provide insights and
        visualizations. The project involves processing earthquake records, filtering
        data based on user input, and creating various plots to visualize geographical
        and temporal patterns of seismic events.
Revisions: 00 - Addressed errors in user inputs to improve the user experience.
           01 - Plotted multiple plots for visualization
'''
# Import necessary libraries
import csv  # For handling CSV files
from datetime import datetime as dt  # For working with date and time
import matplotlib.pyplot as plt  # For creating plots
import math  # For mathematical operations

def scattered_plot(lats, lngVals, mags):
    """
    Creating a scatter plot of Nuclear Explosion/Rock Burst/Explosion/Earthquake locations.
    Parameters:
        lats (list): List of latitude values.
        lngVals (list): List of longitude values.
        mags (list): List of magnitude values.
    Returns:
        None (displays the scatter plot).
    Plot Description:
        - The x-axis represents the longitude in degrees.
        - The y-axis represents the latitude in degrees.
        - Each data point is sized and colored based on the magnitude.
        - Provides a visual representation of the geographic distribution and 
         intensity of seismic events.
        - The colorbar indicates the magnitude scale.
    """
    # Creating a scatter plot
    plt.scatter(lngVals, lats, s=mags, c=mags, cmap='viridis')
    plt.xlabel('Longitude in Degrees') # Label the x-axis
    plt.ylabel('Latitude in Degrees') # Label the y-axis
    plt.title('Nuclear Explosion/Rock Burst/Explosion/Earthquake Locations') # title
    plt.colorbar(label='Magnitude') # Add a colorbar to indicate the magnitude scale
    plt.show() # Displaying the plot

def scattered_plot_years(select):
    """
    Creating a scatter plot of average earthquake magnitudes over the years.
    Parameters:
        select (list): List of earthquake records.
    Returns:
        None (displays the scatter plot).
    Plot Description:
        - The x-axis represents the years.
        - The y-axis represents the average earthquake 
          magnitudes for each year.
        - Each data point is sized and colored based on the magnitude.
        - Provides insights into the temporal distribution and intensity of
          earthquake events.
    Note:
        - Valid dates and non-missing magnitudes are considered for calculations.
    """
    year_magnitudes = {} # Initialize a dictionary to store magnitudes for each year
    # Iterating through each earthquake record in the selection
    for record in select: # for loop
        if 'Date' in record and is_valid_date(record['Date']):# if case
            year = dt.strptime(record['Date'], '%m/%d/%Y').year # Extracting the year from the date
            # Extract the magnitude, handle missing or invalid Magnitude values
            magnitude = float(record.get('Magnitude', 0))
            # Create an entry in the dictionary for the year if it doesn't exist
            if year not in year_magnitudes:
                year_magnitudes[year] = [] # empty list for dictionary values
            year_magnitudes[year].append(magnitude) # Appending magnitude to year
    # Calculate the average magnitude for each year
    avg_years, avg_mags = zip(*[(year, sum(mags) / len(mags))\
                                for year, mags in year_magnitudes.items()])
    # Creating a scatter plot with years on the x-axis, average magnitudes on 
    #the y-axis, size (magnitude), and color (magnitude)
    plt.scatter(avg_years, avg_mags, s=avg_mags, c= avg_mags, cmap='viridis')
    plt.xlabel('Year') # Label the x-axis
    plt.ylabel('Average Magnitude') # Label y-axis
    # Get the date range from the 'select' data
    valid_dates = [record['Date'] for record in select if 'Date' in record\
                   and is_valid_date(record['Date'])]
    start_date = min(dt.strptime(date, '%m/%d/%Y') for date in valid_dates) # starting date
    end_date = max(dt.strptime(date, '%m/%d/%Y') for date in valid_dates) # ending date
    plt.title(f'Average Nuclear Explosion/Rock Burst/Explosion/Earthquake Magnitudes\n\
              ({start_date.strftime("%m/%d/%Y")} to {end_date.strftime("%m/%d/%Y")})') # title of plot
    plt.colorbar(label='Average Magnitude') # Adding a colorbar to indicate the magnitude scale
    plt.show() # Display the plot

def bar_plot(labels, bar_data):
    """
    Creates and displays a bar plot with longitudes and seismic events.
    Parameters:
        labels (list): List of labels for the x-axis.
        bar_data (list): List of data values for the y-axis.
    Returns:
        None (displays the plot).
    Plot Components:
        - x-axis labeled with 'Longitude Range (degrees)'
        - y-axis labeled with 'Seismic Events'
        - Title: 'Nuclear Explosion/Rock Burst/Explosion/Earthquake'
        - Adjusts the bottom margin for better visibility of x-axis labels
    """
    plt.bar(labels, bar_data) # Create a bar plot
    plt.xlabel('Longitude Range (degrees)') # label x-axis
    plt.ylabel('Seismic Events') # label y-axis
    plt.title('Nuclear Explosion/Rock Burst/Explosion/Earthquake Bar Plot') # title
    plt.subplots_adjust(bottom=0.15) # Adjust the bottom margin
    plt.show() # Displaying the plot

def hist_plot(lngVals, ran):
    """
    Creates and displays a histogram plot.
    Parameters:
        lngVals (list): List of longitude values for the histogram.
        ran (tuple): Tuple representing the range of the histogram.
    Returns:
        None (displays the plot).
    Plot Components:
        - Histogram with specified bins and range
        - x-axis labeled with 'Longitude Range (degrees)'
        - y-axis labeled with 'Number of Events'
        - Title: 'Nuclear Explosion/Rock Burst/Explosion/Earthquake Histogram'
    """
    plt.hist(lngVals, bins=6, range=ran) # Create a histogram plot
    plt.xlabel('Longitude Range (degrees)') # label x-axis
    plt.ylabel('Number of Events') # label y-axis
    # Setting the title of the plot
    plt.title('Nuclear Explosion/Rock Burst/Explosion/Earthquake longitudes Histogram')
    plt.show() # Displaying the plot

def avg_mags_plot(labels, avg_mags):
    """
    Creates and displays a bar plot of average magnitudes.
    Parameters:
        labels (list): List of labels for each bar.
        avg_mags (list): List of average magnitude values.
    Returns:
        None (displays the plot).
    Plot Components:
        - Bar plot with specified labels and average magnitude values
        - x-axis labeled with 'Longitude Range (degrees)'
        - y-axis labeled with 'Average Magnitude'
        - Title: 'Nuclear Explosions/Rock Bursts/Explosion/Earthquakes'
        - Adjusted bottom space for better layout
    """
    plt.bar(labels, avg_mags) # Creating a bar plot
    plt.xlabel('Longitude Range (degrees)') # label x-axis
    plt.ylabel('Average Magnitude') # label y-axis
    # Setting the title of the plot
    plt.title('Average magnitude plot')
    plt.subplots_adjust(bottom=0.15) # Adjust the bottom space for better layout
    plt.show() # Displaying the plot
    
def bar_plot_years(select):
    """
    Creates and displays a bar plot illustrating the number of seismic events per year.

    Parameters:
        select (list): List of earthquake records.

    Returns:
        None: Displays the bar plot.

    Plot Description:
        - The x-axis represents the years.
        - The y-axis represents the number of seismic events in each year.
        - Provides a visual representation of the distribution of seismic events over time.
    """
    # Count the number of events for each year
    year_counts = {}
    for record in select:
        if 'Date' in record and is_valid_date(record['Date']):
            year = dt.strptime(record['Date'], '%m/%d/%Y').year
            if year not in year_counts:
                year_counts[year] = 0
            year_counts[year] += 1

    years, event_counts = zip(*sorted(year_counts.items()))

    # Creating a bar plot
    plt.bar(years, event_counts)
    plt.xlabel('Year')  # Label the x-axis
    plt.ylabel('Number of Seismic Events')  # Label the y-axis
    plt.title('Number of Seismic Events Over the Years')  # Title
    plt.show()  # Displaying the plot

def latitude(select):
    """
   Collects latitude values from user input.
   Parameters:
       select (list): List of earthquake records.
   Returns:
       list: Selected earthquake records based on latitude range.
   """
   # Display instructions for latitude input
    print("SELECT latitude: enter two values separated by comma\
          \nrange is -77.08 through 86.005")
    while True: # while loop
        # Get user input for minimum and maximum latitude values
        mini, maxi = input("Enter minimum/maximum latitude values: ").split(',')
        # taking minimum and maximum from the given input and converting to float
        mini, maxi = min(float(mini), float(maxi)), max(float(mini), float(maxi)) 
        # Check if the entered values are within the valid range
        if not (-77.08 <= mini and maxi <= 86.005): 
            print(f"One or more values out of range <({mini},{maxi})>") # printing
            continue # continue while loop
        d = {'min': mini, 'max': maxi} # Create a dictionary
        # Filter records based on the entered latitude range
        selected = [x for x in select if mini <= float(x['Latitude']) <= maxi]
        # Print accepted information and selected record count
        print(f"Accepted...\n{d}\nSelected {len(selected)} records.\n")
        # Ask user if they want to move on to longitude
        move = input("Want to move on to longitude? Yes/No: ")
        # Handle cases where the user did not provide a response
        if not move:
            move = input("Please respond. Want to move on to longitude? Yes/No: ")
        # Check if user wants to proceed to longitude or stay with latitude
        if move.lower() == 'yes': # if case
            return selected # returning seletcted values
        else: # else case
            continue # continue
    
def longitude(select):
    """
    Collects longitude values from user input.
    Parameters:
        select (list): List of earthquake records.
    Returns:
        list: Selected earthquake records based on longitude range.
"""
    # Display instructions for longitude input
    print("\nSELECT longitude: enter two values separated by comma\
          \nrange is -179.997 through 179.998") 
    while True: # while loop
        # Get user input for minimum and maximum longitude values
        mini, maxi = input("Enter minimum/maximum longitude values: ").split(',')
        # taking minimum and maximum from the given input and converting to float
        mini, maxi = min(float(mini), float(maxi)), max(float(mini), float(maxi))
        if not (-179.997 <= mini and maxi <= 179.998): # Check values are in the valid range
            print(f"One or more values out of range <({mini},{maxi})>") # printing out of range
            continue # continuing loop from start
        # Create a dictionary to represent the selected range
        d = {'min': mini, 'max': maxi}
        # Filter records based on the entered longitude range
        selected = [x for x in select if mini <= float(x['Longitude']) <= maxi]
        # Print accepted information and selected record count
        print(f"Accepted...\n{d}\nSelected {len(selected)} records.\n")
        # Ask user if they want to move on to dates
        move = input("Want to move on to dates? Ok/no: ")
        # Handle cases where the user did not provide a response
        if not move:
            move = input("Please respond. Want to move on to dates? Ok/no: ") # user prompt
        # Check if user wants to proceed to dates or stay with longitude
        if move.lower() == 'ok':
            return selected # return selected if ok
        else: # else case
            continue # continuing the loop

def is_valid_date(date_string):
    """
    Checks if a given date string is a valid date in the format 'mm/dd/yyyy'.
    Parameters:
        date_string (str): Input date string.
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try: # try
        dt.strptime(date_string, '%m/%d/%Y') # Attempt to parse using specified format
        return True # If successful, the date is valid
    except ValueError: # valueError
        return False # If an error occurs during parsing, the date is not valid

def date(select):
    """
    Allows the user to select date ranges within a specified range.

    Parameters:
        select (list): List of records to filter based on date.

    Returns:
        list: Selected records within the specified date range.
    """
    print("\nSELECT date mm/dd/yyyy: enter two values separated by comma\
          \nrange is 01/02/1965 to 12/30/2016") # Display instructions for date input
    while True:  # While loop to handle input validation
        # Get user input for minimum and maximum date values
        mini, maxi = input("Enter minimum/maximum date values: ").split(',')
        # Ensure that the entered dates are valid and parse them into datetime objects
        date1 = min(dt.strptime(mini, "%m/%d/%Y"), dt.strptime(maxi, "%m/%d/%Y"))
        date2 = max(dt.strptime(mini, "%m/%d/%Y"), dt.strptime(maxi, "%m/%d/%Y"))
        # Check if the entered date values are within the allowed range
        if not (dt.strptime("01/02/1965", "%m/%d/%Y") <= date1 and
                date2 <= dt.strptime("12/30/2016", "%m/%d/%Y")):
            print(f"One or more values out of range <({mini},{maxi})>") # if not in range
            continue # continue the loop from starting
        # Creating a dictionary to represent the selected date range
        d = {'min': date1.strftime("%m/%d/%Y"), 'max': date2.strftime("%m/%d/%Y")}
        # Filter records based on the entered date range
        selected = [x for x in select if is_valid_date(x['Date']) and
                    date1 <= dt.strptime(x['Date'], '%m/%d/%Y') <= date2]
        # Print accepted information and the count of selected records
        print(f"Accepted...\n{d}\nSelected {len(selected)} records.\n")
        # Ask the user if they want to move on to Magnitude
        move = input("Want to move on to Magnitude? sure/no: ")
        # Handle cases where the user did not provide a response
        if not move:
            move = input("Please respond. Want to move on to Magnitude? sure/no: ")
        # Check if the user wants to proceed to Magnitude or stay with date
        if move.lower() == 'sure':
            return selected  # Return selected records if 'sure'
        else:
            continue  # Continue the loop if the user chooses not to proceed

def magnitude(select):
    """
    Allows the user to select records within a specified Magnitude range.
    Parameters:
        select (list): List of records to filter based on Magnitude.
    Returns:
        list: Selected records within the specified Magnitude range.
    """
    # Display instructions for Magnitude input
    print("\nSELECT Magnitude: enter two values separated by comma\nrange is 5.5 through 9.1")
    while True:  # While loop to handle input validation
        # Get user input for minimum and maximum Magnitude values
        mini, maxi = input("Enter minimum/maximum Magnitude values: ").split(',')
        # Convert input values to float and ensure they are within the valid range
        mini, maxi = min(float(mini), float(maxi)), max(float(mini), float(maxi))
        if not (mini >= 5.5 and maxi <= 9.1):
            print(f"One or more values out of range <({mini},{maxi})>") # if not in range
            continue # continue loop from starting
        # Create a dictionary to represent the selected Magnitude range
        d = {'min': float(mini), 'max': float(maxi)}
        # Filter records based on the entered Magnitude range
        selected = [x for x in select if mini <= float(x['Magnitude']) <= maxi]
        # Print accepted information and the count of selected records
        print(f"Accepted...\n{d}\nSelected {len(selected)} records.\n")
        # Ask the user if they want to move on to Analysis
        move = input("Want to move on to Analysis? ok/no:  ")
        # Handle cases where the user did not provide a response
        if not move:
            move = input("Please respond. Want to move on to Analysis? ok/no: ") # user prompt
        # Check if the user wants to proceed to Analysis or stay with Magnitude
        if move.lower() == 'ok':
            return selected  # Return selected records if 'ok'
        else: # else case
            print("\nSELECT Magnitude: enter two values separated by comma\
                  \nrange is 5.5 through 9.1")
            continue # continue loop

if __name__ == "__main__":
    print("*** Earthquake Data ***")  # Title of the project
    # Open earthquake and world cities data files for reading
    with open("earthquakesF23.csv", 'r') as e, open('worldcitiesF23.csv', 'r') as w:
        earth = csv.DictReader(e) # Create a DictReader object for earthquake data
        world = csv.DictReader(w) # Create a DictReader object for world cities data
        ear_data = [i for i in earth] # Create a list containing dictionaries of earthquake data
        world_data = [i for i in world] # Create a list containing dictionaries of world cities data
    select = ear_data  # Set the default selection to all earthquake data
    print('Do you want to manually enter the Data selection? Yes/No: ') # printing
    if input().lower() == 'yes': # if case user input
        # If the user wants to manually select data, apply filters based on user input
        select = latitude(select) # calling latitude function
        select = longitude(select) # calling longitude function
        select = date(select) # calling date function
        select = magnitude(select) # calling magnitude function
    # Extract latitude, longitude, and magnitude values from the selected records
    lats = [float(i['Latitude']) for i in select] # latitude values
    lngVals = [float(i['Longitude']) for i in select] # longitude values
    mags = [float(i['Magnitude']) for i in select] # magnitue values
    
    scattered_plot(lats, lngVals, mags) # Scatter plot of earthquake locations
    scattered_plot_years(select) # Scatter plot - average magnitudes over years
    
    start = math.floor(min(lngVals)) # Calculating minimum longitude value
    end = math.ceil(max(lngVals)) # calculating max lonitude value
    bins = 6  # Adjust this based on your requirements
    width = (end - start) / bins # calculating width of bins
    edges = [(int(start + i * width), []) for i in range(1, bins + 1)] # edges
    lngRecs = dict(edges) # Create dictionary to store records for each longitude bin
    # Group records into longitude ranges
    for i in select: # for loop
        for edge, j in lngRecs.items(): # for loop using lngrecs
            if float(i['Longitude']) < edge: # if case
                j.append(i) # appending lngRecs values
                break # breaking loop
    label_formatting = "{:.2f} to\n{:.2f}" # Format labels for the longitude bins
    labels = [label_formatting.format(edge - width, edge) for edge in lngRecs.keys()]
    data = [len(i) for i in lngRecs.values()] # Calculate data for bar plot 
    ranging = (start, end) # range of longitudes
    # Calculating average magnitudes for each longitude bin
    avg_magnitudes = [sum([float(i['Magnitude']) for i in records]) / len(records)\
                      if records else 0 for records in lngRecs.values()]
    
    bar_plot(labels, data) # calling bar plot function
    hist_plot(lngVals, ranging) # calling histogram plot function
    bar_plot_years(select) # calling function
    avg_mags_plot(labels, avg_magnitudes) # caling average magnitude plot function