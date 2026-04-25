# Selecting a column ages =
df['Age'] print("Agescolumn:")
print(ages)
print("\n ")
# Filtering rows
above_25 = df[df['Age'] > 25] print("People with Age >
25:") print(above_25)
print("\n ")

# iloc (integer-based) row_0 =
df.iloc[0]

print("First row using iloc (row index 0):") print(row_0)
print("\n ")
# loc (label-based)
specific_val = df.loc[0, 'Name'] print("City of the person at
index 0:") print(specific_val)
