#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:52:57 2020

@author: johngillan
"""

import sys
import numpy as np
import pandas as pd

season = int(sys.argv[1])
number = int(sys.argv[2])

main_story = sys.argv[3]
phenomena = sys.argv[4]
deaths = sys.argv[5]
grossness = sys.argv[6]

df = pd.read_csv('./xfiles_episodes_full.csv')

episode_location = np.logical_and(df['season'] == season, df['number'] == number)

episode_index = df.index[episode_location]

df.loc[episode_index, 'main_story'] = main_story
df.loc[episode_index, 'phenomena'] = phenomena
df.loc[episode_index, 'deaths'] = deaths
df.loc[episode_index, 'grossness'] = grossness

df.to_csv('./xfiles_episodes_full.csv', index=False)