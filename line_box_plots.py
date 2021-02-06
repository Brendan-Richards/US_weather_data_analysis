import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# creates a line plot for the weather data and saves it in the specified file location 
def make_line_plot(mean_temps, save_folder, filename):
    # clear any figure in matplotlib before plotting
    plt.clf()

    # these are formatting objects for the x-axis tick labels. We just want to display the month and year
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    month_fmt = mdates.DateFormatter('%b %Y')
    years_fmt = mdates.DateFormatter('%b %Y')

    # make a 2 by 2 subplot grid, since we are only plotting 4 of the cities
    length = 2
    height = 2

    fig, axes = plt.subplots(height, length, figsize=(30, 30), sharey=True)

    # count keeps track of how many subplots we have already made
    count = 0

    # for each of these 4 cities create the line plot
    for city in ['Jacksonville', 'Chicago', 'Phoenix', 'Seattle']:

        # grab the axis for the current subplot, the axes are accessed via axes[0,0], axes[1,0], etc.
        ax = axes[count // length, count % length]
        ax.plot(mean_temps['date'], mean_temps[city])
        ax.set_title(city, size=25)

        # this block sets formatting options for the axis tick labels
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(years_fmt)
        ax.xaxis.set_minor_locator(months)
        ax.xaxis.set_minor_formatter(month_fmt)
        for tick in ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(20) 
        for tick in ax.xaxis.get_minor_ticks():
            tick.label.set_fontsize(20) 
        for tick in ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(20)         

        count += 1

        # if we have made 4 plots, quit looping
        if count == 4:
            break

    # set the plot titles
    plt.suptitle('Mean Temperature from July 2014 through July 2015', fontsize=30)
    fig.text(0.5, 0.04, 'Date', ha='center', fontsize=30)
    fig.text(0.04, 0.5, 'Temperature (Degrees Fahrenheit)', va='center', rotation='vertical', fontsize=30)

    # set the x-axis labels to a rotation of 45 degrees 
    fig.autofmt_xdate(rotation=45, which='minor')
    fig.autofmt_xdate(rotation=45, which='major')  

    # save the plot
    plt.savefig(os.path.join(save_folder, filename)) 


# creates a box plot for the weather data and saves it in the specified file location 
def make_box_plot(mean_temps, save_folder, filename):
    # clear any figure in matplotlib before plotting
    plt.clf()

    # create the box plot
    mean_temps.boxplot(fontsize=20, figsize=(16,16), rot=30)

    # set the plot titles and font sizes
    plt.title('Mean Daily Temperature Distribution for July 2014 to July 2015', size=25)
    plt.xlabel('City', size=25)
    plt.ylabel('Temperature (Degrees Fahrenheit)', size=25)

    # save the plot
    plt.savefig(os.path.join(save_folder, filename)) 