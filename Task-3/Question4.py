import numpy as np
import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering' , 'chennai' , 'campus'])
print("INPUT")
print(ser)

ser = ser.str.title()

print("\nOUTPUT")
print(ser.str.cat(sep=' '))
