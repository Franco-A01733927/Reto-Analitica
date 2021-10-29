# %%
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
sns.set_style("white")
sns.displot(data=df, x="customer")
plt.show()
# %%
sns.scatterplot(data=df, x="total_items", y="discount%")
plt.show()
# %%
