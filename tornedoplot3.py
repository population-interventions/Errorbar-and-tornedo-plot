import numpy as np
from matplotlib import pyplot as plt

# Change this to your actual data
variables = [
'Ratio increase in prevalence of cold housing by \n quintile of deprivation (range 1.25 to 1.68)',
'Rate ratio per 1 degree Celsius less than 18 degrees \n for anxiety and depression (range 1.002 to 1.106)',
'Rate ratio per 1 degree Celsius less than 18 degrees \n for respiratory diseases#',
'Average temperature in cold housing (range \n 16.18 to 13.82 degree Celsius)',
'Proportion of time over the year exposed to cold housing \n for blood pressure effect (range 0.215 to 0.463)',
'Proportion of people living in cold housing \n (range 4.72% to 7.02%)',
'Increase in SBP per 1 degree Celsius less that \n 18 degreees (range 0.23 to 0.90 mmHg)',
'Rate ratio per 10 mmHg increase in SBP for \n hypertension related diseases*',
]

base = 6.131494392
#the order of values of 'variables' in the dataframes: 'lows' and 'values' has to match with each other#

lows = np.array([
    base -	3.407245597	/2,
    base -	5.398257994	/2,
    base -	5.548110752	/2,
    base -	6.078269086	/2,
    base -	6.09057442	/2,
    base -	6.097437109	/2,
    base -	6.113894073	/2,
    base -	6.122231288	/2,
])
values = np.array([
    10.98808879	,
    7.817584411	,
    6.593197054,
    6.184760292	,
    6.17718424	,
    6.164756815	,
    6.147789615	,
    6.131537404	,
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
plt.xlim(base - 4, base + 6)
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