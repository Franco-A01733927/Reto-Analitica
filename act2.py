# %%
import numpy as np
import pandas as pd

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

print("La cantidad total de datos en el DataFrame es de: ", df[df.columns[0]].count())


# ------------------- Análisis por variable --------------------------------
# %%
#customer
print("valor mínimo: ", df['customer'].min())
print("valor máximo: ", df['customer'].max())
print("mean: ", df['customer'].mean())
print("median: ", df['customer'].median())
print("std: ", df['customer'].std())

# %%
#order
print("valor mínimo: ", df['order'].min())
print("valor máximo: ", df['order'].max())
print("mean: ", df['order'].mean())
print("median: ", df['order'].median())
print("std: ", df['order'].std())

# %%
#total_items
print("valor mínimo: ", df['total_items'].min())
print("valor máximo: ", df['total_items'].max())
print("mean: ", df['total_items'].mean())
print("median: ", df['total_items'].median())
print("std: ", df['total_items'].std())

# %%
#discount
print("valor mínimo: ", df['discount%'].min())
print("valor máximo: ", df['discount%'].max())
print("mean: ", df['discount%'].mean())
print("median: ", df['discount%'].median())
print("std: ", df['discount%'].std())

# %%
#weekday
print("valor mínimo: ", df['weekday'].min())
print("valor máximo: ", df['weekday'].max())
print("mean: ", df['weekday'].mean())
print("median: ", df['weekday'].median())
print("std: ", df['weekday'].std())

# %%
