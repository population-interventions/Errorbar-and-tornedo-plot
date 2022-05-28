import numpy as np
from matplotlib import pyplot as plt

#lifetime#

# Change this to your actual data
variables = [
'Ratio increase in prevalence of cold housing by \n quintile of deprivation (range 1.185 to 1.5)',
'Average temperature in cold housing (range \n 16.18 to 13.82 degree Celsius)',
'Rate ratio per 1 degree Celsius less than 18 degrees  \n for COPD and LRTI (range 1.009 to 1.218)',
'Increase in SBP per 1 degree Celsius less that \n 18 degreees (range 0.23 to 0.90 mmHg)',
'Total exposure to cold housing (range \n 1/6th to 1/2th of time)',
'Rate ratio per 10 mmHg increase in SBP for CVD*',
'Ratio increase in prevalence of cold housing by \n quintile of deprivation (range 1.185 to 1.5)',
'Proportion of people living in cold housing (±10% SD)',
]

base = 29.894

#the order of values of 'variables' in the dataframes: 'lows' and 'values' has to match with each other#
lows = np.array([
    base -	13.755/2,
    base -	18.038/2,
    base -	22.302/2,
    base -	26.995/2,
    base -	26.400/2,
    base -	27.193/2,
    base -	27.963/2,
    base -	29.290/2,
])
values = np.array([
    165.488,
    41.876,
    73.904,
    32.976,
    33.566,
    33.032,
    32.079,
    30.642,
])

values = np.subtract(values, lows)

# The y position for each variable
ys = range(len(values))[::-1]  # top to bottom

# Plot the bars, one by one
for y, low, value in zip(ys, lows, values):
    # The width of the 'low' and 'high' pieces
    low_width = base - low*2
    high_width = low + value - base

    # Each bar is a "broken" horizontal bar chart
    plt.broken_barh(
        [(base, low_width), (base, high_width)],
        (y - 0.4, 0.8),
        facecolors=['red', 'green'],  # Try different colors if you like
        edgecolors=['black', 'black'],
        linewidth=1,
    )
    x = base + high_width / 2
    if x <= base + 500:
        x = base + high_width + 500
    plt.text(x, y, str(value), va='center', ha='center')

# Draw a vertical line down the middle
plt.axvline(base, color='black')

# Position the x-axis on the top, hide all the other spines (= axis lines)
axes = plt.gca()  # (gca = get current axes)
axes.spines['left'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['bottom'].set_visible(False)
axes.xaxis.set_ticks_position('top')

# Make the y-axis display the variables
plt.yticks(ys, variables)

# Set the portion of the x- and y-axes to show
plt.xlim(base - 25, base + 150)
plt.ylim(-1, len(variables))

# add a legend
import textwrap as wrap

plt.plot(x, y, label="HALYs (thousands) for 2.5th percentile of input parameter", c='red', linewidth=2.0)
leg = plt.legend(loc='best', bbox_to_anchor=(1.1, 0), fontsize='small', fancybox=True, framealpha=0, shadow=True, borderpad=1)
for text in leg.get_texts():
    text.set_color("black")

plt.plot(x, y, label="HALYs (thousands) for 97.5th percentile of input parameter", c='Green', linewidth=2.0)
leg = plt.legend(loc='best', bbox_to_anchor=(1.1, 0), fontsize='small', fancybox=True, framealpha=0, shadow=True, borderpad=1)
for text in leg.get_texts():
    text.set_color("black")

leg.get_lines()[0].set_linewidth(7)
leg.get_lines()[1].set_linewidth(7)

imgpath='.\test.png'
plt.show()
plt.savefig('tornedoplot.png', dpi=300)