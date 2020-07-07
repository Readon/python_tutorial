# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# from IPython import get_ipython

# %%
a = [[1, 2, 3], [4, 5, 6]]


# %%
import numpy as np

a = np.array(a)


# %%

# get_ipython().run_line_magic("matplotlib", "inline")
from matplotlib import pyplot as plt


# %%
plt.plot(a)
plt.show()


# %%

