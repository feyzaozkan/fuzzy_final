# -*- coding: utf-8 -*-
"""dataUnderstanding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mOZxFi3vKISXYxrb7_7m0Ikc_-BKHmGr
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("combined.csv")
#choose sepsis icd as output
df.drop(columns=["Unnamed: 0","sirs","qsofa"],inplace=True)

plt.figure(figsize=(18,42))
plt.subplots_adjust(hspace = .3)
for i, column in enumerate(df.columns, 1):
    plt.subplot(13,2,i)
    sns.histplot(data=df, x=column, hue=df["sepsis_icd"], stat="density", bins=60, common_norm=False, kde=True)

sns.heatmap(df.corr())

#find correlated attributes with sepsis_icd
plt.figure(figsize=(4, 6))
heatmap = sns.heatmap(df.corr()[['sepsis_icd']].sort_values(by='sepsis_icd', ascending=False), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title("Features Correlating with sepsis_icd", fontdict={'fontsize':18}, pad=16);