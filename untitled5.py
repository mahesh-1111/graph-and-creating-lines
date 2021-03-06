# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19l6f0_65qRKRY5GPFeBHwdm56FqKV1h3
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
matplotlib.style.use('ggplot')

data = pd.DataFrame({
    'Age': np.random.randint(18, 60, 1000).astype(int),
    'Experience': np.random.randint(0, 30, 1000).astype(int),
    'Salary$': np.random.randint(10, 100, 1000).astype(int),
    'Bonus': np.random.randint(0, 20, 1000).astype(int),
})

plt.figure(figsize=(8,6))
plt.title('increasing board')
sns.kdeplot(data['Age'])
sns.kdeplot(data['Experience'])
sns.kdeplot(data['Salary$'])
sns.kdeplot(data['Bonus'])
plt.show()

data.head()