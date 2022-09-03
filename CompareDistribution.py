#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chris Nguyen
Script to compare compounds to negative control.
"""

import numpy as np
import pandas as pd
import seaborn
import scipy
import matplotlib.pyplot as plt
import sys


csv_file = sys.argv[1] # argument for use in the command line
data = pd.read_csv(csv_file)

# Plot Distribution of M-000
data[data['Molecule Name']=='M-000'].hist()
control = data[data['Molecule Name']=='M-000']
plt.title('Histogram of Negative Control')
plt.savefig('NegativeControlDistribution.png',bbox_inches='tight')

# statistical test to test if negative control is normal
print(scipy.stats.normaltest(data[data['Molecule Name'] == 'M-000']['Feature_0']))

# Calculate Mann Whitney U Statistic (for no)
result = {}
for compound in data['Molecule Name'].unique():
    if compound == 'M-000':
        continue
    stat, pvalue = scipy.stats.mannwhitneyu(data[data['Molecule Name'] == 'M-000']['Feature_0'].to_numpy(),
                                        data[data['Molecule Name'] == compound]['Feature_0'].to_numpy())
    
    direction_effect = data[data['Molecule Name'] == 'M-000']['Feature_0'].mean() - data[data['Molecule Name'] == compound]['Feature_0'].mean()
    if direction_effect > 0:
        direction_effect = 1
    else:
        direction_effect = -1
        
    result[compound] = [stat,pvalue,direction_effect]
    
# Sort result by pvalue 
rank = pd.DataFrame.from_dict(result,orient='index').sort_values(by=1)
rank.columns = ['mannwhitneyu_stat','mannwhitneyu_pvalue','direction_effect']
rank['mannwhitneyu_pvalue'] = - np.log10(rank['mannwhitneyu_pvalue'])

# Score 
rank['score'] = round((rank['mannwhitneyu_pvalue']/rank['mannwhitneyu_pvalue'].max())*10,1)
rank[['score','direction_effect']].to_csv('MoleculeRank.csv')

# Violin plot 
plt.figure()
violin_plot = seaborn.violinplot(x='Molecule Name',y='Feature_0',data=data,
                   order=['M-000']+rank.index.tolist()
                   ).set(title='Molecule Distribution Sorted by Sigfinicance')
plt.axvline(0.5,0,1,color='gray') # Vertical line to seperate negative control 
plt.axhline(control['Feature_0'].mean(),0,1,color='red',dashes=(2,2)) # Horizontal line at negative control mean

# overlay score
for count, score in enumerate(['Score']+rank['score'].to_list()):
    plt.annotate(score,(count,10),bbox=dict(boxstyle="round", fc="w"))


plt.savefig('MoleculeDistributionByScore.png',bbox_inches='tight')
