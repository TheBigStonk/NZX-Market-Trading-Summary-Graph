import pandas
import matplotlib.pyplot as plt
import numpy


nzx_data = [["NZSX", 150318264.2555, 59185746],["NZSX", 150328264.2555, 59385746], ["NZSX", 170328264.2555, 59985746]]
frame = pandas.DataFrame(nzx_data, columns=["Market", "Value", "Volume"])

frame.plot()
plt.show()

print(frame)