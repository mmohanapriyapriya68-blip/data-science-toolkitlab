import pandas as pd

# From a Dictionary data = {
'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35],
'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)
# Viewing data
print(df.head()) # First 5 rows print("\n

")

print(df.info()) # Summary of data types and non-nulls print("\n

")
print(df.describe()) # Statistical summary (mean,std, min, max)
