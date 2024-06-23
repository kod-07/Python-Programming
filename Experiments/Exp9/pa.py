import numpy as np
import pandas as pd
lst = list(np.random.random(10))
s1 = pd.Series(lst)
d = {
    's1': [10,20,30,40],
    's2' :[30,40,50,60],
    's3' :[70,80,80,90]
}
df = pd.Series(lst)
print("Series using list : ")
print(s1)
print("Data Frame using Dictnary:")
print(df.in_string())
