import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the expression whose roots we want to find

a = 0.5
R = 1.6

# Plot it

tau = np.linspace(-0.5, 1.5, 201)

plt.plot(tau, func(tau))
plt.xlabel("tau")
plt.ylabel("expression value")
plt.grid()
plt.show()

# Use the numerical solver to find the roots

tau_initial_guess = 0.5
tau_solution = fsolve(func, tau_initial_guess)

print "The solution is tau = %f" % tau_solution
print "at which the value of the expression is %f" % func(tau_solution)