import pandas as pd
import sys, os

path = os.path.dirname(sys.executable)

inFile = input('Enter input file: ')
outFile = input('Enter output file: ')
#file = './sample.csv'
df = pd.read_csv(f'{path}/{inFile}')

# with open(inFile,'r') as i:
#     lines = i.readlines()

#def manipulateData(lines):
for col in df.columns:
    df[col] = df[col].replace("\\N", "")
    #df[col] = df[col].str.replace(",", "")
    df[col] = df[col].replace(',', '', regex=True)
    df[col] = df[col].replace('"', '', regex=True)

#processedData = manipulateData(lines)
# with open(outFile,'w') as o:
#     for col in df.columns:
#         o.write(col)

#print(df)

df.to_csv(f'{path}/{outFile}', index=False)