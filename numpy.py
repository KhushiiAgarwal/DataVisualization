import matplotlib as plt
import numpy as np
import pandas as pd

print("Pie Chart")
a=[100,115,140,132]
b=['Explorers','Guardians','Innovators','Vanguards']
c=['Green','Blue','Yellow','Red']
plt.pie(a,labels=b,colors=c)
plt.title("Winners")
plt.show()

print("Scatter Chart")
x=np.arange(5)
y=x**2
plt.xlim(0,10)
plt.ylim(0,100)
plt.scatter(x,y)
plt.title("Sq of no")
plt.show()

print("Bar graph from DataFrame")
df=pd.DataFrame({"1990":[200,250,210],"2000":[210,220,230],"2010":[260,270,280]})
df.index=["Delhi","Mumbai","Kolkata"]
df.plot.bar()
plt.show()


