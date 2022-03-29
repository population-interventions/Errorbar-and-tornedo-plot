import numpy as np
from matplotlib import pyplot as plt

# Change this to your actual data
variables = [
    'Relative difference in prevalence of cold housing in most deprived vs least deprived (1 c.f. 5) (ranging from 1.185 to 1.5)',
    'Average temperature in cold housing (ranging from 15.22 to 16.78 degree Celsius) (see methods text in the paper)',
    'Total exposure to cold housing (ranging from 1/6th to 1/2th)',
    'Relative risk ratio of temperature onto depression and anxiety (from 1.009 to 1.218)',
    'Relative shift of high blood pressure from exposure to indoor cold (from 0.23 to 0.90 mmHg)',
]

base = 3.100560366 
#the order of values of 'variables' in the dataframes: 'lows' and 'values' has to match with each other#
lows = np.array([
    base - 1.966246756/ 2,
    base - 3.088360813/ 2,
    base - 3.084411813/ 2,
    base - 2.809630641/ 2,
    base - 3.079248254/ 2,
])

values = np.array([
5.010249208,
3.112323635,
3.10900483,
7.750298943,
3.111757998,
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
plt.xlim(base - 10, base + 10)
plt.ylim(-1, len(variables))

# add a legend
import textwrap as wrap

plt.plot(x, y, label="Incremental HALYs gain for 2.5th percentile of input parameter", c='red', linewidth=2.0)
leg = plt.legend(loc='best', bbox_to_anchor=(1.1, 0), fontsize='small', fancybox=True, framealpha=0, shadow=True, borderpad=1)
for text in leg.get_texts():
    text.set_color("black")

plt.plot(x, y, label="Incremental HALYs gain for 97.5th percentile of input parameter", c='Green', linewidth=2.0)
leg = plt.legend(loc='best', bbox_to_anchor=(1.1, 0), fontsize='small', fancybox=True, framealpha=0, shadow=True, borderpad=1)
for text in leg.get_texts():
    text.set_color("black")

leg.get_lines()[0].set_linewidth(7)
leg.get_lines()[1].set_linewidth(7)

plt.show()