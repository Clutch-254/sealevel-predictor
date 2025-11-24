# Sea Level Predictor

A Python script that analyzes and visualizes global sea level changes from 1880 to present, with projections extending to 2050. Uses linear regression to show both long-term historical trends and more recent acceleration in sea level rise.

## What It Does

This visualizer creates a comprehensive plot showing:
- **Scatter plot** of actual sea level measurements since 1880
- **Red line** showing the best fit for all historical data (1880-present) extended to 2050
- **Green line** showing the best fit for recent data (2000-present) extended to 2050

The two lines of best fit reveal an important story: sea levels are rising faster now than the historical average suggests.

## Requirements

```bash
pip install pandas matplotlib scipy
```

## Data Format

The script expects `epa-sea-level.csv` with at least two columns:
- `Year` - The year of measurement
- `CSIRO Adjusted Sea Level` - Sea level in inches (adjusted by CSIRO - Commonwealth Scientific and Industrial Research Organisation)

## Usage

```python
from sea_level_predictor import draw_plot

# Create the visualization
draw_plot()  # Saves as 'sea_level_plot.png'
```

## What the Visualization Shows

### The Scatter Plot
Each point represents the actual sea level measurement for that year. You can see the overall upward trend and how measurements have become more precise over time.

### Red Line (Historical Trend)
This uses **all data from 1880 to present** to calculate a line of best fit:
- Shows the long-term average rate of sea level rise
- Extended to 2050 to show what would happen if the historical rate continued
- Represents the baseline trend over the past 140+ years

### Green Line (Recent Trend)
This uses **only data from 2000 onwards** to calculate a separate line of best fit:
- Shows the current rate of sea level rise
- Typically steeper than the red line, indicating acceleration
- Extended to 2050 to show projections based on recent trends
- More relevant for near-term predictions

## The Key Insight

The gap between the red and green lines is significant:
- **Red line**: "If sea levels keep rising at the historical average rate..."
- **Green line**: "If sea levels keep rising at the current rate..."

The green line being steeper shows that sea level rise has accelerated in recent decades, which aligns with climate science showing increased glacial melting and thermal expansion of oceans.

## Technical Details

The script uses `scipy.stats.linregress()` to calculate:
- Slope (rate of sea level rise per year)
- Y-intercept (starting point of the line)
- R-value, p-value, and standard error (statistical measures)

Both regression lines use the simple equation: **y = mx + b**
- m = slope (how much sea level rises each year)
- b = y-intercept (the baseline value)
- x = year

## Output

Saves `sea_level_plot.png` with:
- Figure size: 12x6 inches
- X-axis: 1870 to 2060 (with padding for clarity)
- Y-axis: -1 to 16 inches
- Legend showing both trend lines
- Clear labels and title

## Interpreting the Results

When you run this, look for:
- **How steep is each line?** Steeper = faster sea level rise
- **What's the difference between them?** Shows acceleration in recent decades
- **Where do they predict 2050 levels?** Compare the two predictions
- **How well do the lines fit the data?** Tighter fit = more reliable predictions

## Why Two Time Periods?

- **1880-Present**: Gives the full historical context and long-term trend
- **2000-Present**: Captures recent acceleration and provides more relevant short-term predictions

Using both helps distinguish between:
- Natural long-term trends
- Recent changes potentially driven by human activity

## Real-World Application

This type of analysis helps:
- Climate scientists understand acceleration in sea level rise
- Policy makers plan for coastal infrastructure
- Communities prepare for future flooding risks
- Researchers validate climate models

## Limitations

Remember that linear regression assumes:
- The trend will continue unchanged
- No major disruptions or policy changes
- Historical patterns predict future outcomes

Real sea level rise might be faster or slower depending on future emissions, ice sheet dynamics, and other factors not captured in a simple linear model.

Perfect for learning about climate data visualization, understanding linear regression, or exploring environmental datasets!
