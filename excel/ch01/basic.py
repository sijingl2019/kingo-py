import pandas as pd

s1 = pd.Series(["a", "b", "c", "d"])
print(s1)

s2 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s2)

s3 = pd.Series({"a": 1, "b": 2})

print(s3)

df1 = pd.DataFrame(["a", "b", "c", "d"])
print(df1)
df2 = pd.DataFrame([["a", "A"], ["b", "B"]])
print(df2)
df3 = pd.DataFrame([["a", "A"], ["b", "B"]],
                   columns=["low", "up"],
                   index=[0, 1])
print(df3)

excel_path = "excel\\ch01\\abc.xlsx"
df_abc = pd.read_excel(excel_path, index_col=0, header=0, nrows=2)
print(df_abc)

print('new line')
