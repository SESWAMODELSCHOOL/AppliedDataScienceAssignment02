
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('API_19_DS2_en_csv_v2_4756035.csv',skiprows=4)

dfc = pd.read_csv('Metadata_Country_API_19_DS2_en_csv_v2_4756035.csv')

dfc1 = dfc[~pd.isna(dfc['IncomeGroup'])]
df = df[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code','2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
         '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']]

df['mean'] = df[[ '2005', '2006', '2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019', '2020', '2021']].mean(axis=1)
