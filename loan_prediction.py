import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

test = pd.read_csv("./dataset/test_Y3wMUE5_7gLdaTN.csv")
train = pd.read_csv("t/dataset/train_u6lujuX_CVtuZ9i.csv")

columns = df.columns
head = df.head(20)
print(head)
print(df.describe())
df.findnan()