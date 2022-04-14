
import pandas as pd
from pathlib import Path

basepath = Path('csvfiles/')
files_in_basepath = basepath.iterdir()

file_list = []

for item in files_in_basepath:
    if item.is_file():
        file_list.append(item.name)

for i in range(len(file_list)):
    print(i+1, ". ", file_list[i], sep="")

file_chosen = file_list[int(input("Vælg en fil:"))-1]
file_to_open = basepath / file_chosen

if Path(file_to_open).suffix == ".csv":
    df = pd.read_csv(file_to_open)
else:
    quit()

df['Dato'] = pd.to_datetime(df['Dato'])

df['Minutes'] = df.Dato.dt.strftime('%H:%M')

print(df.head())
