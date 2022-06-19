# ______________________________________________________________ #
## Ishan Saran, Yale School of Medicine                         ##
## Advisor: Dr. Francis Perry Wilson, Professor of Nephrology   ##
##                                                              ##
##                                                              ##
## | 今天是   二零二二年 |                                         ##
## | 星期一   五月十六日 |                                         ##
# ______________________________________________________________ #
from __future__ import division

# Imports
%matplotlib inline
from serpapi import GoogleScholarSearch
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from collections import Counter
import sys
import os
plt.rcParams["figure.figsize"] = (20,10)
from itertools import chain
#import tqdm as tqdm
from colorthief import ColorThief

GoogleScholarSearch.SERP_API_KEY = "45c0e77d4c9ac27751d8cf0d1d38a522e46191deda1cb8b1ff6c71a0955e0b62"
query = GoogleScholarSearch({"q": "acute kidney injury"})
print("...\n")
data = query.get_dict()
if data['search_metadata']['status'] == "Success":
    print("Search successful!")
data.keys()


