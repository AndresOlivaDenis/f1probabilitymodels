# f1probabilitymodels
The F1 Probability Models (f1probabilitymodels) is a Python package designed to estimate probabilities for various Formula 1 racing outcomes based on historical data. The model provides statistical insights into race results, starting grid positions, and conditional probabilities based on championship standings.

# Repository Structure

```bash
f1probabilitymodels/
├── data/                
├── notebooks/
│   └── pe_historical_data_car_standings_notebook.ipynb
├── f1probabilitymodels/
│   ├── historical_data_processing
│   ├── probability_estimates
│   ├── probability_estimates
│   └── tests
├── README.md
└── requirements.txt
```

# Getting Started

### Prerequisites
- Python 3.8+
- pandas, matplotlib, scipy, numpy, requests, beautifulsoup4.

### Install dependencies:
```bash
pip install -r requirements.txt
```

# Quick start example

```python
import pandas as pd
from f1probabilitymodels.historical_data_processing.historical_data_processing_m1 import process_historical_historical_data_m1
from f1probabilitymodels.probability_estimates.pe_historical_data import ProbabilityEstimateHistoricalData

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
```

### Historical data processing

```python
df_data, df_data_all = process_historical_historical_data_m1()
print(df_data)
```

```
OUT:
       raceId                     race_name        driverRef  qualifying_position  grid position  positionOrder  driver_standing_position  constructor_standing_position  round    year                                                url
0          18  Australian Grand Prix - 2008         hamilton                  1.0     1        1              1                       1.0                            1.0      1  2008.0  http://en.wikipedia.org/wiki/2008_Australian_G...
1          18  Australian Grand Prix - 2008         heidfeld                  5.0     5        2              2                       2.0                            3.0      1  2008.0  http://en.wikipedia.org/wiki/2008_Australian_G...
2          18  Australian Grand Prix - 2008          rosberg                  7.0     7        3              3                       3.0                            2.0      1  2008.0  http://en.wikipedia.org/wiki/2008_Australian_G...
3          18  Australian Grand Prix - 2008           alonso                 12.0    11        4              4                       4.0                            4.0      1  2008.0  http://en.wikipedia.org/wiki/2008_Australian_G...
4          18  Australian Grand Prix - 2008       kovalainen                  3.0     3        5              5                       5.0                            1.0      1  2008.0  http://en.wikipedia.org/wiki/2008_Australian_G...
...       ...                           ...              ...                  ...   ...      ...            ...                       ...                            ...    ...     ...                                                ...
25715    1089     Italian Grand Prix - 2022  kevin_magnussen                 19.0    16       16             16                      12.0                            7.0     16  2022.0  http://en.wikipedia.org/wiki/2022_Italian_Gran...
25716    1089     Italian Grand Prix - 2022        ricciardo                  8.0     4       \N             17                      14.0                            5.0     16  2022.0  http://en.wikipedia.org/wiki/2022_Italian_Gran...
25717    1089     Italian Grand Prix - 2022           stroll                 18.0    12       \N             18                      18.0                            9.0     16  2022.0  http://en.wikipedia.org/wiki/2022_Italian_Gran...
25718    1089     Italian Grand Prix - 2022           alonso                 10.0     6       \N             19                       9.0                            4.0     16  2022.0  http://en.wikipedia.org/wiki/2022_Italian_Gran...
25719    1089     Italian Grand Prix - 2022           vettel                 17.0    11       \N             20                      13.0                            9.0     16  2022.0  http://en.wikipedia.org/wiki/2022_Italian_Gran...
[25720 rows x 12 columns]
```

### Estimation parameters and ProbabilityEstimateHistoricalData object initialization

```python
# Estimation parameters
driver_championship_standing = 1
constructor_championship_standing = 1
ci = 0.95

# ProbabilityEstimateHistoricalData
pehd = ProbabilityEstimateHistoricalData(df_data, subdatset_params_dict=None)
```

### Starting grid probabilities

```python
grid_estimate = pehd.compute_grid_estimate(
    driver_championship_standing=driver_championship_standing,
    constructor_championship_standing=constructor_championship_standing,
    ci=ci
)
print(f"Prob of Pole position: {grid_estimate.ci_position_probabilities.loc[1].to_dict()}")
print(f"Prob top 3 starting:  {grid_estimate.ci_cum_position_probabilities.loc[3].to_dict()}")
print(f"Prob top 5 starting:  {grid_estimate.ci_cum_position_probabilities.loc[5].to_dict()}")
print(f"Prob top 10 starting:  {grid_estimate.ci_cum_position_probabilities.loc[10].to_dict()}")
```

```
OUT:
Prob of Pole position: {'Probability': 0.4117647058823529, 'CI_lower': 0.40989346312401503, 'CI_upper': 0.4136359486406908}
Prob top 3 starting:  {'Probability': 0.7977941176470588, 'CI_lower': 0.7962670005420235, 'CI_upper': 0.799321234752094}
Prob top 5 starting:  {'Probability': 0.8823529411764705, 'CI_lower': 0.8811279252359389, 'CI_upper': 0.883577957117002}
Prob top 10 starting:  {'Probability': 0.9485294117647056, 'CI_lower': 0.9476893039959291, 'CI_upper': 0.9493695195334821}
```

### Race results probabilities

```python
race_estimate = pehd.compute_race_estimate(
    driver_championship_standing=driver_championship_standing,
    constructor_championship_standing=constructor_championship_standing,
    ci=ci
)

print(f"Prob of winning race: {race_estimate.ci_position_probabilities.loc[1].to_dict()}")
print(f"Prob finishing race in top 3: {race_estimate.ci_cum_position_probabilities.loc[3].to_dict()}")
print(f"Prob finishing race in top 5: {race_estimate.ci_cum_position_probabilities.loc[5].to_dict()}")
print(f"Prob finishing race in top 10: {race_estimate.ci_cum_position_probabilities.loc[10].to_dict()}")
```

```
OUT:
Prob of winning race: {'Probability': 0.5110294117647058, 'CI_lower': 0.5091287958976682, 'CI_upper': 0.5129300276317434}
Prob finishing race in top 3: {'Probability': 0.7941176470588235, 'CI_lower': 0.7925802642548587, 'CI_upper': 0.7956550298627882}
Prob finishing race in top 5: {'Probability': 0.8713235294117646, 'CI_lower': 0.8700504094573611, 'CI_upper': 0.8725966493661681}
Prob finishing race in top 10: {'Probability': 0.9338235294117646, 'CI_lower': 0.9328783500266856, 'CI_upper': 0.9347687087968436}
```

### Race result given grid starting position probabilities

```python
grid = 3
race_estimate_given_grid = pehd.compute_conditioning_on_grid_race_estimate(
    grid=grid,
    driver_championship_standing=driver_championship_standing,
    constructor_championship_standing=constructor_championship_standing,
    ci=ci
)

print(f"Prob of winning race (starting from {grid}): {race_estimate_given_grid.ci_cum_position_probabilities.loc[1].to_dict()}")
print(f"Prob finishing race in top 3 (starting from {grid}): {race_estimate_given_grid.ci_cum_position_probabilities.loc[3].to_dict()}")
print(f"Prob finishing race in top 5 (starting from {grid}): {race_estimate_given_grid.ci_cum_position_probabilities.loc[5].to_dict()}")
print(f"Prob finishing race in top 10 (starting from {grid}): {race_estimate_given_grid.ci_cum_position_probabilities.loc[10].to_dict()}")
```


```
OUT:
Prob of winning race (starting from 3): {'Probability': 0.32432432432432434, 'CI_lower': 0.3194984886751883, 'CI_upper': 0.32915015997346037}
Prob finishing race in top 3 (starting from 3): {'Probability': 0.7297297297297298, 'CI_lower': 0.7251515400502577, 'CI_upper': 0.7343079194092019}
Prob finishing race in top 5 (starting from 3): {'Probability': 0.8648648648648649, 'CI_lower': 0.8613405728064057, 'CI_upper': 0.8683891569233241}
Prob finishing race in top 10 (starting from 3): {'Probability': 0.9189189189189189, 'CI_lower': 0.9161049973666647, 'CI_upper': 0.921732840471173}
```


