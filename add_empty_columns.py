#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:02:04 2020

@author: johngillan
"""

import numpy as np
import pandas as pd

df = pd.read_csv('./xfiles_episodes.csv')

df['main_story'] = np.zeros(len(df))
df['phenomena'] = np.zeros(len(df))
df['deaths'] = np.zeros(len(df))
df['grossness'] = np.zeros(len(df))
df['mulder_correct'] = np.zeros(len(df))
df['driver'] = np.zeros(len(df))
df['state'] = np.zeros(len(df))

# df.to_csv('./xfiles_episodes_full.csv', index=False)
