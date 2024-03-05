# ========= Task 1.4 ===========
# Two compilation errors appear in this file.
# As well as a runtime error, the other a logical error.

import pandas as pd
import matplotlib.pyplot as plt 


data = pd.read_csv("granite_ternary.csv")

# Compilaton Errors as plt should be plot and date should be dat
    # Specficially a SyntaxError and AttributeError
dat.plt(kind= 'scatter', x='longitude', y='latitude')


# Runtime KeyError as granite does not exist as a column nested in data
# Logical Error as would only print out the first letter of each value in granite.
for value in data['granite']:
    print(value[0]) 