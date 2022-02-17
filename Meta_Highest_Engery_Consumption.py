# Import your libraries
import pandas as pd
from functools import reduce

# Start writing code
df1 = fb_eu_energy
df2 = fb_asia_energy
df3 = fb_na_energy

#Join 3 dfs together by outer_join
df_list = [df1, df2, df3]

df = reduce(lambda left,right: pd.merge(left, right, how = 'outer', on = ['date']), df_list)

# Sum the consumption columns together ignoring na
df1 = df.assign(total_cspt = lambda df: df.loc[:,'consumption_x':'consumption'].sum(axis = 1))

# Return the rows where the total_cspt = max values of this column
df1.sort_values('total_cspt', ascending = [False]).query('total_cspt == total_cspt.max()')
