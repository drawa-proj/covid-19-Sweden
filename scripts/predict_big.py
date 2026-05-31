import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

#data
df = pd.read_csv("../data/compact.csv")
df = df[df["country"] == "Sweden"].copy()
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date").sort_index()

#getting smoothed to avoid noise
series_all = df["new_cases_smoothed"]
series = series_all["2020-02-01":"2025-12-31"]


#model 1-------------- (trained 2020(feb)-2023), forecasts from 2024
train1 = series[:"2023-12-31"]
test1 = series["2024-01-01":]

fit1 = ARIMA(train1, order=(0,1,1)).fit()

fore_model_1 = fit1.forecast(steps=len(test1))
fore_model_1.index = test1.index


#model 2---------------------(trained 2020(feb)-2024), forecasts from 2025
train2 = series[:"2024-12-31"]
test2 = series["2025-01-01":]
#the same kind of model
fit2 = ARIMA(train2, order=(0,1,1)).fit()

fore_model_2 = fit2.forecast(steps=len(test2))
fore_model_2.index = test2.index



#stats
mae1 = mean_absolute_error(test1, fore_model_1)
mae2 = mean_absolute_error(test2, fore_model_2)
print("MAE model 1:", mae1)
print("MAE model 2:", mae2)


#plotting
plt.figure(figsize=(13, 5))

plt.plot(series_all.index, series_all.values, color="gray", label="actual cases")

plt.plot(fore_model_1.index, fore_model_1.values,color="red",  linestyle="--",  label="ARIMA trained on 2020–2023")

plt.plot(fore_model_2.index,fore_model_2.values,color="blue",linestyle="--", label="ARIMA trained on 2020–2024")

plt.title("New COVID-19 cases in Sweden (ARIMA)")
plt.ylabel("New cases (smoothed)")
plt.xlim(pd.Timestamp("2020-01-01"), pd.Timestamp("2025-12-31"))
plt.legend()
plt.xlabel("date")
plt.tight_layout()
plt.savefig("../images/sweden_arima_all.png", dpi=150)
plt.show()