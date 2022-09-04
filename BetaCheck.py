import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

"""mean=[np.log(float(input("what is your mean value?")))]"""
"""Alternatively, specify the value of mean here"""
mean=np.log(1.010937979)
print("Mean", mean)

def getSd(UCI, LCI):
    sigma=(np.log(UCI)-np.log(LCI))/3.96
    return sigma

sd=getSd(1.0000,1.0617)
print("Standard Deviation:", sd)

# estimate parameters of beta dist.
def getAlphaBeta(mu, sigma):
    alpha = mu**2 * ((1 - mu) / sigma**2 - 1 / mu)

    beta = alpha * (1 / mu - 1)

    return [alpha, beta]

a1=getAlphaBeta(mean, sd)  
"""e.g. mean: 0.520323374, std: 0.0418978878 for RR 1.52 (95% CI: 1.44-1.72)"""

a=a1[0]
print('Alpha:',a1[0])
b=a1[1]
print('Beta:',a1[1])

# Set the shape paremeters
# Generate the value between
x = np.linspace(beta.ppf(0.01, a, b),beta.ppf(0.99, a, b), 100)
#
# Plot the beta distribution
plt.figure(figsize=(7,7))
plt.xlim(0.00001, 0.07)
plt.plot(x, beta.pdf(x, a, b), 'r-')
plt.title('Beta Distribution', fontsize='15')
plt.xlabel('Probability', fontsize='15')
plt.ylabel('Values of Random Variable X (0, 1)', fontsize='15')
plt.show()