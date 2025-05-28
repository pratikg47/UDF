import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go


np.random.seed(10)
data = np.random.normal(101,12,200)

fig = plt.figure(figsize =(10,7))

fig= plt.boxplot(data)

wd.save_image(plt)
