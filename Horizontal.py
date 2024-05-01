import matplotlib.pyplot as pl

import numpy as np

import pandas as pd

label=['Indu', 'Roshesh', 'Sahil', 'Monisha', 'Maya']

per-[94,85,92,96,78]

index mp.arange(len(label))

pl.barh(index,per,color=['b','k','g','y','c'])

pl.xlabel("Student name", fontsize=4,)

pl.ylabel("Percentage",fontsize=6)

pl.yticks(index, label)

pl.title "SCOREBOARD"

pl.show()
