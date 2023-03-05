# -*- coding: utf-8 -*-
"""finalEval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1teu0GIUHk4AgQ1vTv__GCUFD0ke51kN2
"""

import pandas as pd 
df = pd.read_csv("y_actual_pred.csv")

df["predicted_"] = [1 if x >= 0.5 else 0 for x in df["predicted"] ]

train = df.loc[:687]
test = df.loc[688:]

from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class_names=[0,1]

#confusion matrix and scores for testing data
cnf_matrix = metrics.confusion_matrix(train["actual"],train["predicted_"])
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix for training data', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

from sklearn import metrics
print("f1: ",metrics.f1_score(train["actual"],train["predicted_"]))
print("acc: ",metrics.accuracy_score(train["actual"],train["predicted_"]))
print("p: ",metrics.precision_score(train["actual"],train["predicted_"]))
print("r: ",metrics.recall_score(train["actual"],train["predicted_"]))

cnf_matrix = metrics.confusion_matrix(test["actual"],test["predicted_"])
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix for testing data', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

print("f1: ",metrics.f1_score(test["actual"],test["predicted_"]))
print("acc: ", metrics.accuracy_score(test["actual"],test["predicted_"]))
print("p: ", metrics.precision_score(test["actual"],test["predicted_"]))
print("r: ", metrics.recall_score(test["actual"],test["predicted_"]))
