import pandas as pd
import sys, os

path = os.path.dirname(sys.executable)

inFile = input('Enter input file: ')
outFile = input('Enter output file: ')

df = pd.read_csv(f'{path}/{inFile}')

for col in df.columns:
    df[col] = df[col].replace("\\N", "")
    df[col] = df[col].replace(',', '', regex=True)
    df[col] = df[col].replace('"', '', regex=True)

#print(df)

df.to_csv(f'{path}/{outFile}', index=False)
