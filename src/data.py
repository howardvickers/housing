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
drop_counties = ['fips', 'area', 'mhi_2016', 'mhi_per_2016']
us_unem = unem_rates[:1].drop(columns=drop_counties)
cols_us_unem = ['states', '2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
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

unem_fifty = states_rates.T
unem_fifty.columns = unem_fifty.iloc[0]
unem_fifty = unem_fifty.iloc[1:]
unem_major = unem_fifty[major_states]
unem_delta = unem_major.pct_change()
unem_delta = unem_delta.iloc[1:]




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




sales = pd.read_csv('Sale_Prices_County.csv')

us_state_abbrev =   {
                    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL',
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


sales_major = sales_major.drop('2018-04', axis=1)


# sst = sales_major.T


sales_major_states = sales_major.groupby('state').mean()

year_ends = ['2008-12', '2009-12', '2010-12', '2011-12', '2012-12', '2013-12', '2014-12', '2015-12', '2016-12', '2017-12']

sales_annual = sales_major_states[year_ends]


# sales_annual = sales_major[year_ends]

sales_delta = sales_annual.T.pct_change()
sales_delta.replace([NaN, inf], 0)





pop = pd.read_excel('nst-est2017-01.xlsx')
pop.to_csv('pop.csv')

pop = pd.read_csv('pop.csv')
pop.columns = pop.iloc[2]
pop = pop.iloc[3:59]

pop = pop.reset_index()
pop = pop.drop(['index', 2], axis=1)
pop.columns = ['state', 'census_2010', 'estimate_base', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']

pop[['census_2010', 'estimate_base', '2010']] = pop[['census_2010', 'estimate_base', '2010']].apply(pd.to_numeric)



pop_states = pop.iloc[5:]
pop_states.state = pop_states.state.str.split('.').str[1]
pop_states = pop_states.replace({'state': us_state_abbrev})

pop_states.state = pop_states.state.str.lower()


pop_2009 = pd.read_excel('rank01.xls')
pop_2009.to_csv('pop2009.csv')
pop_2009 = pd.read_csv('pop2009.csv')

pop_2009.columns = pop_2009.iloc[8]

pop_2009 = pop_2009.iloc[9:61]
pop_2009 = pop_2009.reset_index()

pop_2009 = pop_2009.drop(['index', 8, 'Rank'], axis=1)

pop_2009.columns = ['state', '2009']

pop_2009['2009'] = pop_2009['2009'].apply(pd.to_numeric)

pop_2009 = pop_2009.replace({'state':us_state_abbrev})
pop_2009.state = pop_2009.state.str.lower()

pop_complete = pd.merge(pop_states, pop_2009, on=['state'])

new_order_cols = ['state', 'census_2010', 'estimate_base', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
pop_complete = pop_complete[new_order_cols]

chg_typ_cols = ['census_2010', 'estimate_base', '2009','2010']
pop_complete[chg_typ_cols] = pop_complete[chg_typ_cols].astype(float)
pop_complete = pop_complete.drop(['census_2010', 'estimate_base'], axis=1)

pop_pivot = pop_complete.T

pop_pivot.columns = pop_pivot.iloc[0]

pop_pivot = pop_pivot.iloc[1:]

pop_major = pop_pivot[major_states]
