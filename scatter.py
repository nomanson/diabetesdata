# Opgave: import excel to dataframe and store in csv format.Tjek.
# Opgave: lav scatter plot på blodsukker værdier over døgnet
"""
Kulhydratratio

Kulhydratratioen fortæller, hvor mange gram kulhydrat 1 enhed hurtigtvirkende insulin dækker.
Udregning: 500/antal enheder insulin pr. døgn = antal gram kulhydrat pr. enhed hurtigtvirkende insulin.

Insulinfølsomhed

Insulinfølsomhed fortæller, hvor mange mmol/l 1 enhed hurtigtvirkende insulin sænker blodsukkeret med.

Udregning: 100/antal enheder insulin pr. døgn = antal mmol/l, som 1 enhed hurtigtvirkende insulin sænker blodsukkeret.

https://videncenterfordiabetes.dk/viden-om-diabetes/type-1-diabetes/behandling/insulin/beregning-af-insulindosis

"""

import pandas as pd
import numpy
from scipy import stats

import matplotlib.pyplot as plt
pd.options.display.max_rows = 60
print(pd.options.display.max_rows)

from pathlib import Path

data_folder = Path("csvfiles/")
file_to_open = data_folder / "diab_data.csv"

df = pd.read_csv(file_to_open)

df['Dato'] = pd.to_datetime(df['Dato'])

df['Minutes'] = df.Dato.dt.strftime('%H-%M')

x = numpy.mean(df['Blodsukkermåling (mmol/L)'])
y = numpy.median(df['Blodsukkermåling (mmol/L)'])
z = stats.mode(df['Blodsukkermåling (mmol/L)'])

print(x)
print(y)
print(z)

plt.hist(df['Blodsukkermåling (mmol/L)'], 25)
plt.show()



"""
df.plot(kind = 'scatter', x = 'Minutes', y = 'Blodsukkermåling (mmol/L)')

plt.show()
"""