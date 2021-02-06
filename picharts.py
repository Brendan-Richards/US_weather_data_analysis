import pandas as pd
import matplotlib.pyplot as plt
import os

# this function takes a pandas dataframe, df, and
# computes a new column that represents the deviation of 
# actual max temperature values from the historical average values
def calculate_deviation(df):
    df['max_temp_deviation'] = df['actual_max_temp'] - df['average_max_temp'] 

# this function classifies all the max temperature deviations in the dataframe, df, as either: 
# Normal, Moderately Warm, Moderately Cold, Unseasonably Warm, or Unseasonably Cold
# and stores this as a new column in the dataframe
def classify_deviation(df):
    # this list will hold all the classifications
    classes = []
    
    # loop through each row of the dataframe
    for index, row in df.iterrows():
        # d holds this row's deviation value
        d = row['max_temp_deviation']

        # classify d based on which range it falls into
        if d <= 3 and d >= -3:
            classes.append('Normal')
        elif d <= 8 and d > 3:
            classes.append('Moderately Warm')
        elif d >= -8 and d < -3:
            classes.append('Moderately Cold')
        elif d > 8:
            classes.append('Unseasonably Warm')
        elif d < -8:
            classes.append('Unseasonably Cold')

    # store the classes in a new column in the dataframe
    df['max_temp_deviation_class'] = classes
    
    
# this function creates picharts for each city showing the percentages of days 
# that are warmer and cooler than the historical average
def make_picharts(cities, save_folder, filename):

    # create the deviation columns for each city in the cities dictionary
    for city in cities.keys():
        calculate_deviation(cities[city])
        classify_deviation(cities[city])

    # make a 2 by 5 subplot grid, since we are plotting all of the (10) cities
    length = 2
    height = 5

    fig, axes = plt.subplots(height, length, figsize=(20, 30))

    # map each of the deviation classes to a unique RGB color tuple
    color_map = {
        'Normal': (0.9, 0.9, 0.9),
        'Moderately Warm': (1.0, 0.25, 0),
        'Unseasonably Warm': (1.0, 0, 0),
        'Moderately Cold': (0, 0.75, 1.0),
        'Unseasonably Cold': (0, 0.3, 1.0)
    }

    # keeps track of how many subplots we have made
    count = 0

    # for each city
    for city in cities.keys():

         # grab the axis for the current subplot, the axes are accessed via axes[0,0], axes[1,0], etc.
        ax = axes[count // length, count % length]
        
        # holds the counts for the 5 possible classes for this city
        value_counts = cities[city]['max_temp_deviation_class'].value_counts()
        # the labels to use for this pichart
        labels = ['Normal', 'Moderately Warm', 'Unseasonably Warm', 'Moderately Cold', 'Unseasonably Cold']
        # the percentages of days in each class for this city 
        sizes = [(value_counts[label] / 365) for label in labels]
        # the colors that each segment of the pichart should have
        colors = [color_map[label] for label in labels]
        
        ax.set_title(city, size=20)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
        
        count += 1

    # save the figure in the provided file location   
    plt.savefig(os.path.join(save_folder, filename), facecolor='white')
    