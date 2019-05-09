import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

test = pd.read_csv("test_Y3wMUE5_7gLdaTN.csv")
train = pd.read_csv("")

columns = df.columns
head = df.head(20)
print(head)
print(df.describe())
df.findnan()