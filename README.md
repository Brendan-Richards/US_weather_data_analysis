This repository contains analysis of weather data for 10 U.S. cities from July 1st 2014 to June 30th 2015. The dataset (which can be found here: https://github.com/fivethirtyeight/data/tree/master/us-weather-history) contains daily and historical temperature and precipitation information. 

The python files in this repository can be used to recreate the visualizations displayed in this readme. Simply run: "python create_visualizations.py" to create the images and save them in the images folder. Required dependencies are: Matplotlib and Pandas.

<h1>The Analysis</h1>

I began my analysis by loading the data into pandas dataframes, one for each city. The data required very little cleaning, I just checked the dataframes for null values and converted the date column into a pandas datetime format for easy manipulation. I began my analysis by plotting the mean daily temperatures for several cities. This is shown in the following figure for Jacksonville, Chicago, Phoenix, and Seattle.


    
![png](README_files/README_6_0.png)
    


As one would expect, the temperatures vary from city to city, but each curve has the same basic V shape with a central dip around January. To further investigate the variability, I created box plot distributions for each of the cities.


    
![png](README_files/README_8_1.png)
    


By comparing the box sizes, this plot shows that cities such as Chicago and Seattle have much more weather variability throughout the year than cities such as Jacksonville and Los Angeles. Given the large differences between cities, it's more useful to compare each city's current data to its own historical data than to any other cities. With this in mind, I wanted to find out if these data show a warming trend (as one would expect due to climate change). 

For each day, the dataset contains the average maximum temperature since 1880 and the actual maximum temperature that occurred. I subtracted the former from the latter to calculate the daily maximum temperature's deviation from the historical average maximum temperature. A large number of positive deviations (the actual maximum temperature is larger than the historical average) indicates a warming trend and likewise a large number of negative deviations (the historical average is larger than the actual maximum temperature) indicates a cooling trend. 

To visualize this I took the deviations and classified them as:<br>
   &nbsp; "Normal" if the deviation was between 3 and -3 degrees, <br>
   &nbsp; "Moderately Warm" if between 8 and 3 degrees, <br>
   &nbsp; "Moderately Cold" if between -8 and -3 degrees, <br>
   &nbsp; "Unseasonably Warm" if greater than 8 degrees, and <br>
   &nbsp; "Unseasonably Cold" if less than -8 degrees 

For each of the 10 cities in the dataset I created pie charts showing the percent of days falling into each of these 5 classes. This is shown in the following figure. 


    
![png](README_files/README_14_1.png)
    
<h1>Conclusion</h1>

These charts show less obvious warming than I would have expected. New York, Philadelphia, Chicago, and Houston show roughly equal percentages of warm and cool days and Indianapolis even showed a substantially cooler year than average. However Seattle, Phoenix, Jacksonville, Charlotte, and Los Angeles show quite severe heat trends. The warming trend would likely be even more apparent if more years were included in this analysis. In conclusion, I have found that looking at the weather data from July 2014 to July 2015, 9 of the 10 cities had a normal or warmer than average year overall.


