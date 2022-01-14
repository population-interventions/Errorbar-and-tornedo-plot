import numpy as np
from matplotlib import pyplot as plt

# Change this to your actual data
variables = [
    'Change in input paramter 1 (ranging % to % increase)',
    'Change in input paramter 2 (ranging % to % increase)',
    'Change in input paramter 3 (ranging % to % increase)',
    'Change in input paramter 4 (ranging % to % increase)',
    'Change in input paramter 5 (ranging % to % increase)',
    'Change in input paramter 6 (ranging % to % increase)',
    'Change in input paramter 7 (ranging % to % increase)',
    'Change in input paramter 8 (ranging % to % increase)',
]

base = 3000
#the order of values of 'variables' in the dataframes: 'lows' and 'values' has to match with each other#
lows = np.array([
    base - 1633 / 2,
    base - 500 / 2,
    base - 246 / 2,
    base - 150 / 2,
    base - 43 / 2,
    base - 37 / 2,
    base - 36 / 2,
    base - 35 / 2,
])

values = np.array([
    1633,
    500,
    246,
    150,
    43,
    37,
    36,
    35,
])

# The y position for each variable
ys = range(len(values))[::-1]  # top to bottom

# Plot the bars, one by one
for y, low, value in zip(ys, lows, values):
    # The width of the 'low' and 'high' pieces
    low_width = base - low
    high_width = low + value - base

    # Each bar is a "broken" horizontal bar chart
    plt.broken_barh(
        [(low, low_width), (base, high_width)],
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
plt.xlim(base - 1000, base + 1000)
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