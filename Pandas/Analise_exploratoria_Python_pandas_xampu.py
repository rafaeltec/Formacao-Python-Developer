import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")

from google.colab import files
arq = files.upload()
df = pd.read_excel("xampu_phrase-match_br_2024-04-30.xlsx")
# prompt: Com o DataFrame df: volume more tham 20

df[df['Volume'] > 10]
from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['index']
  ys = series['Keyword Difficulty']
  
  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = _df_73.sort_values('index', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Intent')):
  _plot_series(series, series_name, i)
  fig.legend(title='Intent', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('index')
_ = plt.ylabel('Keyword Difficulty')


# @title Keyword Difficulty

from matplotlib import pyplot as plt
df['Keyword Difficulty'].plot(kind='hist', bins=20, title='Keyword Difficulty')
plt.gca().spines[['top', 'right',]].set_visible(False)