import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')
import numpy as np

###############################################################################
values = [
    'Eradication of indoor cold (current)',
    'Statin for adults',
    'Mandatory Tick program',
    'Diuretic for adults',
    'ACE inhibitor for adults',
    'Beta-blocker for adults',
    'Community heart health program',
    'TEXT ME advice',
    'Lifestyle program for adults',
    'Dietary advice for adults',
    'Phytocterol for adults',
]

#ticks for the y-axis#
y = np.array([
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
])

#ticks for the x-axis#
x = np.array([
    4.9,
    4.1,
    3.8,
    3.7,
    3.6,
    2.95,
    0.14,
    0.15,
    0.05,
    0.05,
    0.05,
])

#SD for error bars - preprocess the SDs - before putting in here, SE = (upper limit – lower limit) / 3.92# 
dy = np.array([[
    2.2,
    1.93877551,
    0.816326531,
    2.040816327,
    1.479591837,
    1.326530612,
    0.07,
    0.076530612,
    0.010204082,
    0.010204082,
    0.010204082,
],
[
    4.9,
    1.93877551,
    0.816326531,
    2.040816327,
    1.479591837,
    1.326530612,
    0.062,
    0.076530612,
    0.010204082,
    0.010204082,
    0.010204082,
]]
)


plt.errorbar(x, y, xerr=dy, fmt='s', color='black',
             ecolor='black', elinewidth=2, capsize=3);
plt.yticks(y,values);
plt.grid(False);
plt.xlabel('HALYs (+high and low UI)')
imgpath='.\test.png'
plt.show()
plt.savefig('errorplot.png', dpi=300)
