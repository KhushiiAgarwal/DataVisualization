import matplotlib.pyplot as pl

import numpy as np numpya

import pandas as pd

df=pd.DataFrame({"1990": [200,250,210],"2000" )

[210,220,230], "2010" : [260,270,280]}

df.index=["Delhi", "Mumbai","Kolkata"]

df.plot.bar()

pl.show()
