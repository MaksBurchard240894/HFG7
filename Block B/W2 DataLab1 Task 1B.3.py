import numpy as np
import pandas as pd
from io import StringIO

np.genfromtxt("C:/Users/maksb/OneDrive/Documents/GitHub/2024-25b-fai1-adsai-MaksBurchard240894/Block B/diabetic_data_py.csv",None,"#",",")

df = pd.read_csv("C:/Users/maksb/OneDrive/Documents/GitHub/2024-25b-fai1-adsai-MaksBurchard240894/Block B/diabetic_data_py.csv", sep=",")

pd.DataFrame.dtypes

pd.DataFrame.info(df)

#df.to_html('temp.html')
#print(df.to_string())

