'''
# "DEPRECATED" code from book:
import pandas as pd 
from pandas_datareader import wb

df = wb.get_indictors()[['id', 'name']]
df = df[df.name == 'Individuals using thr Internet (% of population)']
print(df)'''

# World Bank Data "wbdata" New code:
import pandas as pd
import wbdata

indicators = wbdata.get_indicators()
df = pd.DataFrame(indicators.items(), columns=["id", "name"])
df = df[df["name"] == "Individuals using the Internet (% of population)"]
print(df)
