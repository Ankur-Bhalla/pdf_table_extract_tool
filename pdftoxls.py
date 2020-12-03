import camelot
import pandas as pd

file = "Food Calories List.pdf"  # file to be processed, to be placed in the project folder
tables = camelot.read_pdf(file, pages='1-end')  # reads pdf

df = pd.DataFrame(tables[0].df)  # dataframe for first page(table)
for i in range(1, tables.n):
    df2 = pd.DataFrame(tables[i].df)  # dataframe for next page(table)
    df = pd.merge(df, df2, how='outer')  # merge dataframes
    for col in df.columns:
        df[col] = df[col].str.replace('\n', '')
df.to_csv("Output.csv")  # output to csv
