from TausGenerator import TausGenerator
from tests import Tests
import numpy as np
import matplotlib.pyplot as plt

g = TausGenerator(8, 3, 13, 1000)

outputs = g.generate()

plt.figure()
plt.hist(outputs, 20, density=True, alpha=0.75)

plt.xlabel('PRN')
plt.ylabel('Probability')
plt.title('Histogram of PRN from Tausworthe Generator')
plt.grid(True)
plt.savefig('PDF.png')
plt.close()

test = Tests(outputs)
test.test_Chi2_goodness_iid()
test.test_up_and_down()
test.test_above_below_mean()
test.test_correlation()


plt.figure()
plt.scatter(outputs[:-1], outputs[1:])

plt.xlabel(r'$U_{i}$')
plt.ylabel(r'$U_{i+1}$')
plt.title('Scatter plot of adjacent PRNs')
plt.savefig('adjacent.png')
plt.close()

# Box-Muller transformation
# https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
U1 = outputs[:-1]
U2 = outputs[1:]
Z = np.sqrt(-2.*np.log(U1))*np.cos(2*np.pi*U2)
Z = Z[np.isfinite(Z)]
print(Z)

plt.figure()
plt.hist(Z, 20, density=True, alpha=0.75)

plt.xlabel('PRN')
plt.ylabel('Probability')
plt.title('Histogram of Normal Distribution after Box-Muller Transform')
plt.grid(True)
plt.savefig('normal.png')
plt.close()



