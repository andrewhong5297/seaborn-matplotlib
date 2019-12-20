# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:59:57 2019

@author: honandre

This is ordered by most useful to most niche plots, as well as difficulty of use.

General Notes:
1) Figsize is used to determine how large the picture shows in console (if items look squished increase the size)
2) Use help(data.distplot) to see documentation, replace distplot with whatever function you want.
3) Jitter is generally an addition on graphs to show a confidence interval of sorts
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_style("ticks") #darkgrid, whitegrid, dark, white, ticks. RC is for more customization of the graphic

# reading the data
data = pd.read_excel(r'F:\Treasury Risk Rotation Docs\Market Pricing\LR Nov 15 (2018-2019 data) (cleaned).xlsx')

"""histogram, KDE, or Rug: histogram are the bars, KDE is the distribution line (True to show, false to hide). Rug is the frequency in each bar."""
#sns.distplot(data["Cushion"], hist=True, kde= False, rug=True, fit= stats.gamma);
"""line plot: same as bar plot but line instead (not in 0.8, only in 0.9)"""
#plt.figure(figsize=(10,6))
#sns.lineplot(x="Date", y="Pro-Forma Amount ($mm)", data=data)
"""joint plot: just a histogram on top of a scatter, though this can be played with"""
#df = pd.DataFrame(data, columns=["Cushion", "Amount($mm)"])
#with sns.axes_style("ticks"):
#    sns.jointplot(x="Cushion",y = "Amount($mm)", data = df, kind = "hex", color="k");
# kind can be none for scatter, or hex, kde, 
"""pair plot: quick correlation/regression code to see where to investigate more"""
#sns.pairplot(data,x_vars=["Amount($mm)", "Pro-Forma Amount ($mm)" , "DG", "RWA%"],y_vars=["Cushion"], kind = "reg")
"""heat map: two categories and a value, good for tracking values on a time series of products/projects"""
#data_heat = data.pivot(index="P&T",columns="Date",values="Cushion")
#f,ax=plt.subplots(figsize=(18,12)) #fig print size
#sns.heatmap(data_heat, annot=True, linewidths=.5,ax=ax)
"""box plot: best for statistical summary comparisons across categories (yes/no, industries, products)"""
#sns.boxplot(x="Date",y="Pro-Forma Amount ($mm)", palette= ["b"], data = data)
#sns.despine(offset=10, trim=True)
"""matplotlib california scatterplot: good for adding size and heatmap elements to a scatter"""
#data.plot(kind="scatter", x = "Cushion", y = "Amount($mm)", alpha = 1, s=data["Pro-Forma Amount ($mm)"], figsize=(10,10), c="DG", cmap=plt.get_cmap("jet"), colorbar=True,)
#plt.legend()
"""Scatterplot: same as above but in seaborn instead of matplotlib"""
#cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
#ax = sns.scatterplot(x="Cushion",y="Amount($mm)",
#                     hue="DG", size="Pro-Forma Amount ($mm)", 
#                     palette=cmap, sizes=(40,400), alpha=0.4, height = 6, data=data)
"""Relplot: same as above but for categories instead of continuous coloring"""
#sns.relplot(x="Cushion",y="Amount($mm)",
#                     hue="Industry", size="Pro-Forma Amount ($mm)", 
#                     palette=cmap, sizes=(40,400), alpha=0.4, height = 6, data=data)
"""lmplot: best for multiple regression lines if a scatter has multiple groups (i.e. industries)"""
#g = sns.lmplot(x="Cushion",y="Amount($mm)",hue="Industry",truncate=True, height =5, data=data)
#g.set_axis_labels("Cushion Used (bps)", "Size of Facility ($mm)")

"""Cat Plot: error (ANOVA) on top of line or box plot"""

"""Swarmplot: show to relationship between a continuous and categorical variable"""

"""Stripplot: https://seaborn.pydata.org/examples/jitter_stripplot.html """

"""Violinplot: https://seaborn.pydata.org/examples/simple_violinplots.html """

"""Clustermap: https://seaborn.pydata.org/examples/structured_heatmap.html """

"""Facetgrid: has physics use, or probability use see https://seaborn.pydata.org/examples/many_facets.html"""
