import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read in data
unem = pd.read_csv('../data/unemployment_usda_2007_2017.csv')

# remove first rows with data sources mentioned
unem = unem.iloc[6:]

# rename columns
unem.columns = unem.iloc[0]

# drop the row with the column names
unem = unem.iloc[1:]

# reset index
unem = unem.reset_index(drop=True)

# rename the index
unem.columns.name = 'index'

cols_drop =     ['Rural_urban_continuum_code_2013', 'Urban_influence_code_2013', 'Metro_2013', 'Civilian_labor_force_2007', 'Employed_2007', 'Unemployed_2007', 'Civilian_labor_force_2008', 'Employed_2008', 'Unemployed_2008', 'Civilian_labor_force_2009', 'Employed_2009', 'Unemployed_2009', 'Civilian_labor_force_2010', 'Employed_2010', 'Unemployed_2010', 'Civilian_labor_force_2011', 'Employed_2011', 'Unemployed_2011',
                'Civilian_labor_force_2012', 'Employed_2012', 'Unemployed_2012', 'Civilian_labor_force_2013', 'Employed_2013', 'Unemployed_2013', 'Civilian_labor_force_2014', 'Employed_2014', 'Unemployed_2014', 'Civilian_labor_force_2015', 'Employed_2015', 'Unemployed_2015', 'Civilian_labor_force_2016', 'Employed_2016', 'Unemployed_2016', 'Civilian_labor_force_2017', 'Employed_2017', 'Unemployed_2017']

unem_rates = unem.drop(columns = cols_drop)
unem_rates.columns = ['fips', 'state', 'area', 'u_2007', 'u_2008', 'u_2009','u_2010', 'u_2011', 'u_2012', 'u_2013', 'u_2014', 'u_2015', 'u_2016', 'u_2017', 'mhi_2016', 'mhi_per_2016']

cols_num = ['u_2007', 'u_2008', 'u_2009','u_2010', 'u_2011', 'u_2012', 'u_2013', 'u_2014', 'u_2015', 'u_2016', 'u_2017', 'mhi_2016', 'mhi_per_2016']

unem_rates[cols_num] = unem_rates[cols_num].apply(pd.to_numeric)

# plot just us rates over years
drop_counties = ['fips', 'state', 'area', 'mhi_2016', 'mhi_per_2016']
us_unem = unem_rates[:1].drop(columns=drop_counties)
cols_us_unem = ['2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
us_unem.columns = cols_us_unem
plt.plot(us_unem.iloc[0])
plt.show()

unem_rates.area = unem_rates.area.str.lower()
unem_rates.state = unem_rates.state.str.lower()

states =  ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
          "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
          "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
          "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
          "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
          "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
          "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
          "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
states = [x.lower() for x in states]

states_rates = unem_rates[unem_rates['area'].isin(states)]

states_rates = states_rates.drop(drop_counties, axis=1)
states_rates.columns = cols_us_unem
plt.plot(states_rates.iloc[0:])

county_rates = unem_rates[~unem_rates['area'].isin(states)]

states.append('united states')
county_rates = unem_rates[~unem_rates['area'].isin(states)]
county_rates.area = county_rates.area.str.split(' county').str[0]


# convert original xls to csv...
fips = pd.read_excel('../data/fips.xls')
fips.to_csv('../data/fips.csv')

# can assume that csv file exists from here on...
fips = pd.read_csv('../data/fips.csv')
fips.columns = fips.iloc[0]
fips = fips.iloc[1:]

fips = fips.reset_index()
fips = fips.drop(['index', 0], axis=1)

fips['fips'] = fips[['FIPS State', 'FIPS County']].apply(lambda x: ''.join(x), axis=1)
fips = fips.drop(columns = ['FIPS State', 'FIPS County'])
fips.columns = ['state', 'county', 'fips']
fips.county = fips['county'].str.lower()
fips = fips.replace({'state': us_state_abbrev})
fips.state = fips['state'].str.lower()

# unem_rates_fips = pd.merge(unem_rates,fips, on=['county','state'])
# unem_rates_fips = pd.merge(fips,unem_rates, on=['state','county'])


sales = pd.read_csv('Sale_Prices_County.csv')

us_state_abbrev =   {
                    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                    'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME',
                    'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
                    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                    'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
                    'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
                    }

sales = sales.replace({'StateName': us_state_abbrev})
sales.StateName = sales.StateName.str.lower()
sales.RegionName = sales.RegionName.str.lower()

sales = sales.drop(['RegionID', 'SizeRank'], axis=1)

sales = sales.rename(index=str, columns={'RegionName' : 'county', 'StateName': 'state'})

sales_fips = pd.merge(sales, fips, how='left', on=['county', 'state'])
sales_fips.groupby('state').count()
major_states = ['ca', 'co', 'fl', 'ga', 'md','ny', 'va']
sales_major = sales_fips[sales_fips['state'].isin(major_states)]
sales_major.groupby('state').count()
plt.plot(sales_major.iloc[0:]) # this gives each county - need to sum them for each state 
