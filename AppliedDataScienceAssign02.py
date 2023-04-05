
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('API_19_DS2_en_csv_v2_4756035.csv',skiprows=4)

dfc = pd.read_csv('Metadata_Country_API_19_DS2_en_csv_v2_4756035.csv')

dfc1 = dfc[~pd.isna(dfc['IncomeGroup'])]

