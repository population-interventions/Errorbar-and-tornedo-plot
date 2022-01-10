import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')
import numpy as np

###############################################################################
values = [
    'Statin for adults',
    'Mandatory Tick program',
    'Diuretic for adults',
    'ACE inhibitor for adults',
    'Beta-blocker for adults',
    'Aspirin for adults',
    'Eradication of indoor cold (current)',
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
    12,
])

#ticks for the x-axis#
x = np.array([
    4.1,
    3.8,
    3.7,
    3.6,
    2.95,
    2.0,
    1.95,
    1.2,
    0.15,
    0.05,
    0.05,
    0.05,
])

#SD for error bars - preprosess the SDs - before putting in here SE = (upper limit – lower limit) / 3.92# 
dy = np.array([
1.93877551,
0.816326531,
2.040816327,
1.479591837,
1.326530612,
1.683673469,
1.173469388,
0.637755102,
0.076530612,
0.010204082,
0.010204082,
0.010204082,
])

plt.errorbar(x, y, xerr=dy, fmt='s', color='g',
             ecolor='g', elinewidth=2, capsize=3);
plt.yticks(y,values);
plt.grid(False);
plt.xlabel('HALYs (+high and low UI)')
plt.show()