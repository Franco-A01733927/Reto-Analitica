# %%
import math
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kneed import KneeLocator

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
sns.set_style("white")

# %%
sns.heatmap(df.corr(),annot=True)

# %%
T_items = df[df["total_items"] < 29] 
sns.boxplot(data=T_items,x="weekday",y="total_items")

# %%
discount_porc = df[df["discount%"] > 0]
sns.boxplot(data=discount_porc,x="weekday",y="discount%")

# %%
Hour = df[df["hour"] > 0]
sns.boxplot(data=Hour,x="weekday",y="hour")

# %%
dfp = df[["total_items", "discount%", "Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters suggested by knee method: {k}")

kmeans = KMeans(n_clusters=k).fit(df[["total_items", "discount%", "Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]])
sns.scatterplot(data=df, x="weekday", y="hour", hue=kmeans.labels_)
plt.show()
# %%
cluster0 = df[kmeans.labels_==0]
print(cluster0.describe())

cluster1 = df[kmeans.labels_==1]
print(cluster1.describe())

cluster2 = df[kmeans.labels_==2]
print(cluster2.describe())

cluster3 = df[kmeans.labels_==3]
print(cluster3.describe())

# %%
sns.boxplot(data=cluster0[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()
sns.boxplot(data=cluster1[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()
sns.boxplot(data=cluster2[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()
sns.boxplot(data=cluster3[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()

# %%
sns.histplot(data=cluster0, x= 'weekday')
plt.show()
sns.histplot(data=cluster1, x= 'weekday')
plt.show()
sns.histplot(data=cluster2, x= 'weekday')
plt.show()
sns.histplot(data=cluster3, x= 'weekday')
plt.show()
# %%
sns.histplot(data=cluster0, x= 'hour')
plt.show()
sns.histplot(data=cluster1, x= 'hour')
plt.show()
sns.histplot(data=cluster2, x= 'hour')
plt.show()
sns.histplot(data=cluster3, x= 'hour')
plt.show()
