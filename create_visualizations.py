import pandas as pd
import os
import line_box_plots
import picharts


if __name__=='__main__':
    # the name of the folder where the data is stored
    data_folder = 'data'
    image_folder = 'images'

    # create a a dictionary where the keys are the U.S. city names from the dataset and the values are pandas dataframes for those cities 
    cities = dict()
    cities['Charlotte'] = pd.read_csv(os.path.join(data_folder, 'KCLT.csv'), parse_dates=["date"])
    cities['Los Angeles'] = pd.read_csv(os.path.join(data_folder, 'KCQT.csv'), parse_dates=["date"])
    cities['Houston'] = pd.read_csv(os.path.join(data_folder, 'KHOU.csv'), parse_dates=["date"])
    cities['Indianapolis'] = pd.read_csv(os.path.join(data_folder, 'KIND.csv'), parse_dates=["date"])
    cities['Jacksonville'] = pd.read_csv(os.path.join(data_folder, 'KJAX.csv'), parse_dates=["date"])
    cities['Chicago'] = pd.read_csv(os.path.join(data_folder, 'KMDW.csv'), parse_dates=["date"])
    cities['New York'] = pd.read_csv(os.path.join(data_folder, 'KNYC.csv'), parse_dates=["date"])
    cities['Philadelphia'] = pd.read_csv(os.path.join(data_folder, 'KPHL.csv'), parse_dates=["date"])
    cities['Phoenix'] = pd.read_csv(os.path.join(data_folder, 'KPHX.csv'), parse_dates=["date"])
    cities['Seattle'] = pd.read_csv(os.path.join(data_folder, 'KSEA.csv'), parse_dates=["date"])

    # create a dataframe where the columns are the cities and rows are the actual mean temperatures 
    mean_temps = pd.DataFrame()
    for city in cities.keys():
        mean_temps[city] = pd.Series(cities[city]['actual_mean_temp'].values)

    # lastly add the date column
    mean_temps['date'] = cities[city]['date']

    # make the line plots and the box plot from the readme
    line_box_plots.make_line_plot(mean_temps, image_folder, 'lineplot.png')
    line_box_plots.make_box_plot(mean_temps, image_folder, 'boxplot.png')

    # create the picharts
    picharts.make_picharts(cities, image_folder, 'pie_plots.png')
    
