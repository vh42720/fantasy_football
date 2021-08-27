"""
Collect data from this website
Thanks to the wonderful work of Ben Dominguez, the collecting
data process is streamlined through his github page.
The main question in this stage is: Which data to use?


Reference
---------
https://github.com/fantasydatapros/data
"""

import pandas as pd

# Getting the data
df = pd.read_csv('https://raw.githubusercontent.com/fantasydatapros/data/master/yearly/2019.csv')

