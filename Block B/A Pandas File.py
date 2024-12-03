import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    ["Olivia", 25, "Eindhoven"],
    ["Ethan", 30, "Breda"],
    ["Sophia", 35, "Warsaw"]
]

columns = ["Name", "Age", "City"]

df = pd.DataFrame(data, columns=columns)

print(df)