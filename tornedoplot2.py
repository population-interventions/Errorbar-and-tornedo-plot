import numpy as np
from matplotlib import pyplot as plt

# Change this to your actual data
variables = [
'Ratio increase in prevalence of cold housing by quintile \n of deprivation (range 1.185 to 1.5)',
'Rate ratio per 1 degree Celsius less than 18 degrees \n for anxiety and depression (range 1.009 to 1.218)',
'Rate ratio per 1 degree Celsius less than 18 degrees  \n for COPD and LRTI (range 1.009 to 1.218)',
'Increase in SBP per 1 degree Celsius less than 18 degrees \n (range 0.23 to 0.90 mmHg)',
'Total exposure to cold housing (range \n 1/6th to 1/2th of time)',
'Rate ratio per 10 mmHg increase in SBP for CVD*',
'Average temperature in cold housing (range \n 16.18 to 13.82 degree Celsius)',
'Proportion of people living in cold housing (±10% SD)'
]

base = 4.290029898
#the order of values of 'variables' in the dataframes: 'lows' and 'values' has to match with each other#
lows = np.array([
    base-	2.68377164 /2,
    base-	3.739989931 /2,
    base-	3.965418513 /2,
    base-	4.207185241 /2,
    base-	4.226358211/2,
    base-	4.254237965 /2,
    base-	4.283891663 /2,
    base-   4.288657159/2,
])
values = np.array([
    6.854710919,
    9.029254082,
    5.651844467,
    4.372718127,
    4.360970456,
    4.326466278,
    4.296111502,
    4.29140391
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
    if x <= base + 50:
        x = base + high_width + 50
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
plt.xlim(base - 2, base + 5.5)
plt.ylim(-1, len(variables))

# add a legend
import textwrap as wrap

plt.plot(x, y, label="Relative risk comparing HALYs between SES1 and SES5 for 2.5th percentile of input parameter", c='red', linewidth=2.0)
leg = plt.legend(loc='best', bbox_to_anchor=(1.1, 0), fontsize='small', fancybox=True, framealpha=0, shadow=True, borderpad=1)
for text in leg.get_texts():
    text.set_color("black")

plt.plot(x, y, label="Relative risk comparing HALYs between SES1 and SES5 for 97.5th percentile of input parameter", c='Green', linewidth=2.0)
leg = plt.legend(loc='best', bbox_to_anchor=(1.1, 0), fontsize='small', fancybox=True, framealpha=0, shadow=True, borderpad=1)
for text in leg.get_texts():
    text.set_color("black")

leg.get_lines()[0].set_linewidth(7)
leg.get_lines()[1].set_linewidth(7)

imgpath='.\test.png'
plt.show()
plt.savefig('tornedoplot.png', dpi=300)