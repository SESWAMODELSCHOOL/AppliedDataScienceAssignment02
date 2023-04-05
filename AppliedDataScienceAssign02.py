
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

#df_year, df_country = data_ingestion(df, 'Population, total')


for ind in selected_indicators:
    df_year, df_country = data_ingestion(df, ind)
    
    for i in df_year.columns:
        sns.swarmplot(y='Country Name',x=i, data=df_year.loc[countries, :].reset_index())
    
    plt.title(ind)
    plt.xlabel('2005-2021')
    plt.show()

for ind in selected_indicators:
    df_year, df_country = data_ingestion(df, ind)
    for i in countries:
        plt.plot(df_country[i], label=i)

    plt.title(ind)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xticks(rotation=90)
    plt.show()

df1 = df.groupby(['Country Name','Indicator Name'])['mean'].mean().unstack()

plt.figure(figsize=(10,7))
sns.heatmap(df1[selected_indicators].corr(), cmap='viridis', linewidths=.5, annot=True)




# ## Correlation Graph of Countries for "Arable Land" Indicator

df_year, df_country = data_ingestion(df, 'Arable land (% of land area)')

plt.figure(figsize=(10,7))
sns.heatmap(df_country[countries].corr(), cmap='viridis', linewidths=.5, annot=True)

# getting data ready. removing some Regions and join data to get only the countries data.

df2 = df1.merge(dfc1, left_on=df1.index, right_on='TableName', how='inner')
df2.index = df2['TableName']


for i in df2[selected_indicators]:
    sns.barplot(x='TableName', y=i, data=df2[i].sort_values(ascending=False)[:10].reset_index())
    plt.xticks(rotation=90)
    plt.xlabel(i)
    plt.title('Top 10 countries with respect to ' + str(i))
    plt.show()


