#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate test data.

Normal Negative Control.
M-001 similar distribution as M-000, with the same mean.
M-002 mean less than M-000.
M-003 mean greater than M-000.
"""

import pandas as pd 
import numpy as np

test_data = pd.DataFrame(np.random.normal(4, 2, size=(100, 1)), columns=['Feature_0'])
test_data['Molecule Name'] = 'M-000'


for molecule,mean in [('M-001',4),('M-002',1),('M-003',9)]:
    molecule_data = pd.DataFrame(np.random.normal(mean, 1, size=(15, 1)), columns=['Feature_0'])
    molecule_data['Molecule Name'] = molecule
    test_data = test_data.append(molecule_data)

test_data[['Molecule Name','Feature_0']].to_csv('test_data.csv',index=False)