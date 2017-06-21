# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:54:32 2017

"""

import pandas as pd


def diff_series(ser1, ser2, verbose = True):
    assert isinstance(ser1, pd.Series)
    assert isinstance(ser2, pd.Series)    
    

def diff_df_merge(tab1, tab2, on = None, verbose = True):
    ''' retourne les valeurs avec des éléments '''
    print("\n ***** différence d'appartenance aux tables")
    assert isinstance(tab1, pd.DataFrame)
    assert isinstance(tab2, pd.DataFrame)
    merge = tab1.merge(tab2, on=on, indicator=True, how='outer')
    if verbose:
        print('appartenance aux deux bases : \n', merge._merge.value_counts(), '\n')

    output = merge[merge['_merge'] != 'both']
    del output['_merge']
    return output


def diff_columns(tab1, tab2, on = None, verbose = True):
    ''' étudie la différence de colonnes'''
    assert isinstance(tab1, pd.DataFrame)
    assert isinstance(tab2, pd.DataFrame) 
    cols1 = set(tab1.columns)
    cols2 = set(tab2.columns)
    not_in_1 = cols2 - cols1
    not_in_2 = cols1 - cols2
    in_both = cols1 & cols2
    print('\n ***** différence des colonnes')
    if len(not_in_1 | not_in_2) == 0:
        print("Les colonnes sont identiques \n")
        return
    if len(not_in_1) == 0:
        print("Toutes les colonnes de la seconde table sont dans la première")
    else:
        phrase = "Les colonnes suivante sont dans la seconde table et pas dans la première :"
        print(phrase + '\n\t' + '\n\t'.join(not_in_1))
        
    if len(not_in_2) == 0:
        print("Toutes les colonnes de la première table sont dans la seconde")
    else:
        phrase = "Les colonnes suivante sont dans la seconde table et pas dans la première :"
        print(phrase + '\n\t' + '\n\t'.join(not_in_2))



def diff_df_values(tab1, tab2, on=None, verbose = True):
    ''' 
        effectue la différence entre les valeurs des deux dataframe.
        Le travaille est effectué sur les colonnes au même noms uniquement
        retourne les lignes pour lesquelles les informations ne sont pas la même dans les deux
        le paramètre on contient la clé de rapprochement, l'évaluation
        ne se fait que sur idenfiant matché.
    '''
    assert isinstance(tab1, pd.DataFrame)
    assert isinstance(tab2, pd.DataFrame)
    print('\n ***** différence des contenus')
    merge = tab1.merge(tab2, on = on, indicator=True, how='inner')
    if verbose:
        print('On étudie les différences sur', len(merge),
              'lignes qui appartiennent aux deux tables.', 
              # 'Utiliser diff_df_merge pour en savoir plus'
              )

    cols_x = [col for col in merge.columns if col[-2:] == '_x']
    cols_y = [col for col in merge.columns if col[-2:] == '_y']

    merge_y = merge[cols_y].rename(columns=dict(x for x in zip(cols_y, cols_x)))
    
    
    similar = merge[cols_x] == merge_y 
    differents = ~similar.all(axis=1)
    if verbose:
        print("\n Il y a {} differences sur {} entités".format(
            sum(differents),
            len(merge))
            )
        print('\n Par variable cela donne : \n', (~similar).sum())
    
    diff = merge[differents]
    diff[cols_x] = diff[cols_x].mask(similar)
    diff[cols_y] = diff[cols_y].mask(similar)
    diff[cols_x] += ' -> ' + merge_y[differents]
    return diff[cols_x + cols_y]


def all_diff_df(tab1, tab2, on = None, verbose = True):
    diff_df_merge(tab1, tab2, on=on, verbose = verbose)
    diff_df_values(tab1, tab2, on=on, verbose = verbose)


def diff(tab1, tab2, on=None, columns=True, values=True, merge=True):
    if columns:
        diff_columns(tab1, tab2, on=on)
    if merge:
        diff_df_merge(tab1, tab2, on=on)
    if values:
        diff_df_values(tab1, tab2, on=on)


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                     index=[0, 1, 2, 3])
 

df2 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D3', 'D3'],
                     'E': ['C0', 'C1', 'C2', 'C3'],},
                     index=[4, 5, 6, 7])

diff(df1, df2)
#diff(df1, df1)