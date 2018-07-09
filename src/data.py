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
# drop_counties = ['area', 'mhi_2016', 'mhi_per_2016']
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

us_state_abbrev =   {
                    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL',
                    'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME',
                    'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
                    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                    'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
                    'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
                    }

major_states = ['ca', 'co', 'fl', 'ga', 'md','ny', 'va']

unem_fifty_states = unem_rates[unem_rates['area'].isin(states)]

unem_fifty_states = unem_fifty_states.drop(drop_counties, axis=1)
unem_fifty_states.columns = cols_us_unem
plt.plot(unem_fifty_states.iloc[0:])

unem_fifty_t = unem_fifty_states.T
unem_fifty_t.columns = unem_fifty_t.iloc[0]
unem_fifty_t = unem_fifty_t.iloc[1:]
unem_major = unem_fifty_t[major_states]


unem_delta = unem_major.pct_change()
unem_delta = unem_delta.iloc[1:]




county_rates = unem_rates[~unem_rates['area'].isin(states)]

states.append('united states')
county_rates = unem_rates[~unem_rates['area'].isin(states)]
county_rates.area = county_rates.area.str.split(' county').str[0]

drop_mhi = ['mhi_2016', 'mhi_per_2016']
county_rates = county_rates.drop(drop_mhi, axis=1)

cols_counties_unem = ['fips','state', 'county', '2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
county_rates.columns = cols_counties_unem



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




sales = pd.read_csv('../data/Sale_Prices_County.csv')

sales = sales.replace({'StateName': us_state_abbrev})
sales.StateName = sales.StateName.str.lower()
sales.RegionName = sales.RegionName.str.lower()

sales = sales.drop(['RegionID', 'SizeRank'], axis=1)

sales = sales.rename(index=str, columns={'RegionName' : 'county', 'StateName': 'state'})

sales_fips = pd.merge(sales, fips, how='left', on=['county', 'state'])
# sales_fips.groupby('state').count()

# NEED TO THINK ABOUT THIS BELOW
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

# END OF NEED TO THINK


sales_fifty = pd.read_csv('../data/Sale_Prices_State.csv')
sales_fifty.drop(['RegionID', 'SizeRank'], axis=1, inplace=True)
sales_fifty = sales_fifty.rename(index=str, columns={'RegionName': 'state'})
sales_fifty = sales_fifty.replace({'state': us_state_abbrev})
sales_fifty.state = sales_fifty['state'].str.lower()

year_ends_state = ['state','2008-12', '2009-12', '2010-12', '2011-12', '2012-12', '2013-12', '2014-12', '2015-12', '2016-12', '2017-12']
sales_fifty_annual = sales_fifty[year_ends_state]


pop = pd.read_excel('../data/nst-est2017-01.xlsx')
pop.to_csv('../data/pop.csv')

pop = pd.read_csv('../data/pop.csv')
pop.columns = pop.iloc[2]
pop = pop.iloc[3:59]

pop = pop.reset_index()
pop = pop.drop(['index', 2, ], axis=1)
pop.columns = ['state', 'census_2010', 'estimate_base', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
pop.drop(['census_2010', 'estimate_base'], axis=1, inplace=True)
pop[['2010']] = pop[['2010']].apply(pd.to_numeric)



pop_fifty = pop.iloc[5:]
pop_fifty.state = pop_fifty.state.str.split('.').str[1]
pop_fifty = pop_fifty.replace({'state': us_state_abbrev})

pop_fifty.state = pop_fifty.state.str.lower()
pop_fifty = pop_fifty.reset_index()
pop_fifty = pop_fifty.drop('index', axis=1)

pop_2009 = pd.read_excel('../data/rank01.xls')
pop_2009.to_csv('../data/pop2009.csv')
pop_2009 = pd.read_csv('../data/pop2009.csv')

pop_2009.columns = pop_2009.iloc[8]

pop_2009 = pop_2009.iloc[9:61]
pop_2009 = pop_2009.reset_index()

pop_2009 = pop_2009.drop(['index', 8, 'Rank'], axis=1)

pop_2009.columns = ['state', '2009']

pop_2009['2009'] = pop_2009['2009'].apply(pd.to_numeric)

pop_2009 = pop_2009.replace({'state':us_state_abbrev})
pop_2009.state = pop_2009.state.str.lower()

pop_complete = pd.merge(pop_fifty, pop_2009, on=['state'])

new_order_cols = ['state',   '2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
pop_complete = pop_complete[new_order_cols]

chg_typ_cols = ['2009','2010']
pop_complete[chg_typ_cols] = pop_complete[chg_typ_cols].astype(float)
# pop_complete = pop_complete.drop(['census_2010', 'estimate_base'], axis=1)

pop_pivot = pop_complete.T

pop_pivot.columns = pop_pivot.iloc[0]

pop_pivot = pop_pivot.iloc[1:]

# pop_major = pop_pivot[major_states]





# DEBT TO INCOME RATIO
dti = pd.read_csv('../data/household-debt-by-county.csv')
dti['mid'] = (dti.low + dti.high)/2
dti.mid = dti.mid.fillna(4)
dti_keep = dti.groupby(['area_fips', 'year']).mid.mean()
dti_keep = dti_keep.reset_index()
dti_keep.columns = ['fips', 'year', 'dti_avg']


dti_1999 = dti_keep[dti_keep.year == 1999]
dti_1999.drop('year', axis=1, inplace=True)
dti_1999.columns = ['fips', '1999']

dti_2016 = dti_keep[dti_keep.year == 1999]
dti_2016.drop('year', axis=1, inplace=True)
dti_2016.columns = ['fips', '2016']


dti_99_16 = pd.merge(dti_1999, dti_2016, how='left', on='fips')

dti_99_16['incr_99_16'] = (dti_99_16['2016'] - dti_99_16['1999']) / dti_99_16['1999']

state_codes = {
    'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
    'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
    'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
    'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
    'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
    'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
    'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
    'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
    'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
}



dti_fifty = pd.read_csv('../data/household-debt-by-state.csv')
dti_fifty['mid'] = (dti_fifty.low + dti_fifty.high)/2
dti_fifty.mid = dti_fifty.mid.fillna(4)
dti_fifty = dti_fifty.groupby(['state_fips', 'year']).mid.mean()
dti_fifty = dti_fifty.reset_index()
dti_fifty.columns = ['state_fips', 'year', 'dti_avg']

dti_fifty.state_fips = dti_fifty['state_fips'].astype(str)

dti_fifty.state_fips = dti_fifty.state_fips.replace({'1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9':'09'})

state_fips_dict = dict(zip(list(state_codes.values()), list(state_codes.keys())))
dti_fifty['state'] = dti_fifty['state_fips'].map(state_fips_dict)
dti_fifty.state = dti_fifty.state.str.lower()
dti_fifty =  dti_fifty.drop('state_fips', axis=1)
dti_fifty = dti_fifty[['state', 'year', 'dti_avg']]


dti_fifty_1999 = dti_fifty[dti_fifty.year == 1999]
dti_fifty_1999.drop('year', axis=1, inplace=True)
dti_fifty_1999.columns = ['state', '1999']

dti_fifty_2016 = dti_fifty[dti_fifty.year == 2016]
dti_fifty_2016.drop('year', axis=1, inplace=True)
dti_fifty_2016.columns = ['state', '2016']

dti_fifty_99_16 = pd.merge(dti_fifty_1999, dti_fifty_2016, how='left', on='state')

dti_fifty_99_16['incr_99_16'] = (dti_fifty_99_16['2016'] - dti_fifty_99_16['1999']) / dti_fifty_99_16['1999']




sales_fifty_annual['incr'] = (sales_fifty_annual['2017-12'] - sales_fifty_annual['2008-12'] ) / sales_fifty_annual['2008-12']

sales_fifty_annual['incr_5'] = (sales_fifty_annual['2017-12'] - sales_fifty_annual['2012-12'] ) / sales_fifty_annual['2012-12']

sales_incr = sales_fifty_annual[sales_fifty_annual['state', 'incr']]
sales_incr_5 = sales_fifty_annual[sales_fifty_annual['state', 'incr_5']]


sales_incr = sales_fifty_annual.drop(['2008-12', '2009-12', '2010-12', '2011-12', '2012-12',
       '2013-12', '2014-12', '2015-12', '2016-12', '2017-12'], axis=1)


sales_incr = sales_incr[~sales_incr.incr.isnull()]


sales_incr.sort_values(['incr'])


plt.bar(np.arange(len(sales_incr.state)), sales_incr.incr.sort_values())
history
