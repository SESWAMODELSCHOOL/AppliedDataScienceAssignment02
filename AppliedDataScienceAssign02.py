
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
selected_indicators = ['Urban population (% of total population)', 'Urban population growth (annual %)', 'Population, total', 'Population growth (annual %)',
 'Agricultural land (sq. km)', 'Energy use (kg of oil equivalent per capita)','Electric power consumption (kWh per capita)','Access to electricity (% of population)','Forest area (% of land area)','Arable land (% of land area)', 'Agricultural land (% of land area)']

countries = ['Italy','Australia','China','United Arab Emirates','Germany','France',
             'Malaysia','Japan','New Zealand','Morocco','United States','Pakistan','India','Bangladesh','Thailand']

df = df.drop(['Country Code','Indicator Code'], axis=1)

def data_ingestion(df, indicator):
    df1 = df[df['Indicator Name'] == indicator]
    df1 = df1.drop(['Indicator Name'], axis=1)
    df1.index = df1.loc[:, 'Country Name']
    df1 = df1.drop(['Country Name'], axis=1)
    df2 = df1.transpose()
    return df1, df2
