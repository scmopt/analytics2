# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/17neuralprophet.ipynb.

# %% auto 0
__all__ = []

# %% ../nbs/17neuralprophet.ipynb 7
import pandas as pd
from neuralprophet import NeuralProphet, set_log_level

# エラー以外はログメッセージを抑制
set_log_level("ERROR")

from vega_datasets import data
import plotly.express as px
import plotly

# %% ../nbs/17neuralprophet.ipynb 43
# retail = pd.read_csv(`http://logopt.com/data/retail_sales.csv`)
# model = Prophet(seasonality_mode=`multiplicative`).fit(retail)
# future = model.make_future_dataframe(periods=20, freq=`M`)
# forecast = model.predict(future)
# model.plot(forecast);
# #model.plot_components(forecast);
