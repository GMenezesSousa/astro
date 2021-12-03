# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:22:13 2021

@author: gabri
"""
import sys
import scipy.optimize as scp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import random
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

def main():
    dados = pd.read_csv('data.txt', index_col = 0)
    max_neigh = 40
    col = 'purple'
    titulo_dados = 'Dados 1 + 2'
    titulo_ind = ', indicador T'
    titulo_rq = titulo_dados + titulo_ind
    
    t = dados['t']
    w = dados['w']
    n = dados['n']
    g = dados['g']
    tds = pd.concat([t, w], axis = 1)
    
    t_t = t.sample(frac = 0.8, random_state = 0)
    t_v = t.drop(t_t.index)
    
    w_t = w[t_t.index]
    w_v = w.drop(t_t.index)
    
    n_t = n[t_t.index]
    n_v = n.drop(t_t.index)
    
    g_t = g[t_t.index]
    g_v = g.drop(t_t.index)
    
    tds_t = pd.concat([t_t, w_t], axis = 1)
    tds_v = pd.concat([t_v, w_v], axis = 1)
    
    plt.figure()
    a = sns.scatterplot(w_t, n_t, color = col)
    plt.title(titulo_dados)
    a.set_xlabel('EW (mA)')
    a.set_ylabel('log(N)')
    plt.show()
    
    plt.figure()
    a = sns.scatterplot(t_t, n_t, color = col)
    plt.title(titulo_dados)
    a.set_xlabel('T (K)')
    a.set_ylabel('log(N)')
    plt.show()
    
    y = n.values
    X = t.values.reshape(len(t), 1)
    
    knn = KNeighborsRegressor()
    param_grid = {'n_neighbors': np.arange(1, max_neigh + 1)}
    knn_gscv = GridSearchCV(knn, param_grid, cv = 5)
    knn_gscv.fit(X, y)
    print(knn_gscv.best_params_['n_neighbors'])
    print(knn_gscv.best_score_)
    qtest = knn_gscv.cv_results_['mean_test_score']
    qtrain = knn_gscv.cv_results_['mean_train_score']
    f_n = np.arange(1, max_neigh + 1, 1)
    
    plt.figure()
    a = sns.lineplot(f_n, qtest, color = col)
    plt.title(titulo_rq)
    a.set_xlabel('# vizinhos')
    a.set_ylabel('Q Test')
    plt.show()
    
    plt.figure()
    a = sns.lineplot(f_n, qtrain, color = col)
    plt.title(titulo_rq)
    a.set_xlabel('# vizinhos')
    a.set_ylabel('Q Train')
    plt.show()
    
    melhor_n = knn_gscv.best_params_['n_neighbors']
    #melhor_n = 1
    knn2 = KNeighborsRegressor(n_neighbors = melhor_n)
    
    y_train = n_t.values
    X_train = t_t.values.reshape(len(t_t), 1)
    y_test = n_v.values
    X_test = t_v.values.reshape(len(t_v), 1)
    
    knn2.fit(X_train, y_train)
    y_pred = knn2.predict(X_test)
    
    popt, pocv = scp.curve_fit(reta, y_test, y_pred)
    l = reta(y_test, popt[0], popt[1])
    
    print(popt)
    
    plt.figure()
    a = sns.scatterplot(y_test, y_pred, color = col)
    b = sns.lineplot(y_test, l, color = col)
    plt.title(titulo_rq)
    a.set_xlabel('log(N) validação')
    a.set_ylabel('log(N) previsto')
    plt.show()
    
def p1(x, param):
    return (param[0] + param[1]*np.exp(param[2]*x))

def chi(y, y_l):
    return (np.sum((y - y_l)**2))

def chi_red(y, yl):
    return (np.sum(((y - yl)/y)**2))

def reta(x, a, b):
    return (a*x + b)

main()