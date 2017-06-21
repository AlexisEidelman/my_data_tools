# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:03:02 2017

@author: User
"""
import os
import importlib
import pandas as pd

def _read_or_generate_data(path_csv, module, force=False):
    if not os.path.exists(path_csv) or force:
        print('**** Load :', module)
        importlib.import_module(module)
    return pd.read_csv(path_csv)