Script:
CompareDistribution.py - Script that computes scores and plots 
distributions.

python CompareDistribution.py Molecules_dist_JD.csv

Output:
NegativeControlDistribution.png - png of M-000 histogram.

MoleculeDistributionBySigfinicance.png - png of molecules distribution 
scored by score. 

MoleculeRank.csv - csv file that contains a dataframe of molecules ranked 
with score and direction of effect.

About:
Summary.pdf - explains score and MoleculeDistributionBySigfinicance.png plot 

Testing:
GenerateTestData.py - Script that creates the csv file test_data.csv.

test_data.csv - csv file that contains sample data that can be processed 
as the Molecules_dist_JD.csv. M-000 is normally distributed. M-001 has a 
similar distribution as M-000 (no significant difference to M-000). M-002 
has a distribution less than M-000 (significant difference to M-000, 
negative direction of effect). M-003 has a distribution greater than M-000 
(significant difference to M-000, positive direction of effect)
