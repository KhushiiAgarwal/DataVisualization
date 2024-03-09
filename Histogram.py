import matplotlib.pyplot as pl

import numpy as np

x=np.arange(5)

pl.hist(x, orientation='vertical', histtype='step',color='cyan', cumulative=True) pl.title('numbering')

pl.show()
