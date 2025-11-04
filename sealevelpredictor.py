import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    """
    Analyzes and visualizes the global average sea level change since 1880.
    It includes two lines of best fit: one for all data and one for data
    since the year 2000, both predicting the sea level rise through 2050.
    """
    # 1. Use Pandas to import the data from epa-sea-level.csv
    # Use a relative path assuming the file is in the same directory or accessible
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create a scatter plot
    # Set the x and y data
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Create the scatter plot
    ax.scatter(x, y)

    # 3. First Line of Best Fit (All Data: 1880 - Present)
    # Use linregress to get the slope and y-intercept
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(x, y)

    # Create a list of years for the regression line, extending to 2050
    # The max year in the dataset is 2013, so we create a range up to 2050
    # We use numpy style array for the years (equivalent to pandas series/list)
    years_extended = pd.Series(range(1880, 2051))

    # Calculate the predicted sea level rise (y = mx + b)
    line_all = slope_all * years_extended + intercept_all

    # Plot the first line of best fit
    ax.plot(
        years_extended,
        line_all,
        color='red',
        label=f'Best Fit Line (1880-Present)'
    )

    # 4. Second Line of Best Fit (Data from Year 2000 - Present)

    # Filter data from the year 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']

    # Get the slope and y-intercept for the new dataset
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x_2000, y_2000)

    # Create a new list of years for this regression line, starting from 2000 and extending to 2050
    years_2000_extended = pd.Series(range(2000, 2051))

    # Calculate the predicted sea level rise for the 2000+ data
    line_2000 = slope_2000 * years_2000_extended + intercept_2000

    # Plot the second line of best fit
    ax.plot(
        years_2000_extended,
        line_2000,
        color='green',
        label=f'Best Fit Line (2000-Present)'
    )

    # 5. Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Optional: Add a legend for clarity (though not explicitly required)
    ax.legend()
    # Optional: Set limits to ensure all data/lines are clearly visible
    ax.set_xlim(1870, 2060)
    ax.set_ylim(-1, 16)


    # Save image and return fig (don't modify this part)
    plt.savefig('sea_level_plot.png')
    return fig
