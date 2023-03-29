import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import pickle as pk

# Some example data to display
position = pk.load(open("simple position","rb"))

x_f = interp1d(position[2],position[0],'linear')
print(x_f(1/30))

