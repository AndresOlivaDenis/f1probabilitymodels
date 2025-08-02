import pandas as pd

from f1probabilitymodels.historical_data_processing.historical_data_processing_m1 import process_historical_historical_data_m1
from f1probabilitymodels.probability_estimates.pe_historical_data import ProbabilityEstimateHistoricalData

if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    # Historical data processing
    df_data, df_data_all = process_historical_historical_data_m1()
    print(df_data)

    # Estimation parameters
    driver_championship_standing = 1
    constructor_championship_standing = 1
    ci = 0.95

    # ProbabilityEstimateHistoricalData
    pehd = ProbabilityEstimateHistoricalData(df_data, subdatset_params_dict=None)

    # Starting grid probabilities
    grid_estimate = pehd.compute_grid_estimate(
        driver_championship_standing=driver_championship_standing,
        constructor_championship_standing=constructor_championship_standing,
        ci=ci
    )
    print(f"Prob of Pole position: {grid_estimate.ci_position_probabilities.loc[1].to_dict()}")
    print(f"Prob top 3 starting:  {grid_estimate.ci_cum_position_probabilities.loc[3].to_dict()}")
    print(f"Prob top 5 starting:  {grid_estimate.ci_cum_position_probabilities.loc[5].to_dict()}")
    print(f"Prob top 10 starting:  {grid_estimate.ci_cum_position_probabilities.loc[10].to_dict()}")

    # Race results probabilities
    race_estimate = pehd.compute_race_estimate(
        driver_championship_standing=driver_championship_standing,
        constructor_championship_standing=constructor_championship_standing,
        ci=ci
    )

    print(f"Prob of winning race: {race_estimate.ci_position_probabilities.loc[1].to_dict()}")
    print(f"Prob finishing race in top 3: {race_estimate.ci_cum_position_probabilities.loc[3].to_dict()}")
    print(f"Prob finishing race in top 5: {race_estimate.ci_cum_position_probabilities.loc[5].to_dict()}")
    print(f"Prob finishing race in top 10: {race_estimate.ci_cum_position_probabilities.loc[10].to_dict()}")

    # Race result given grid starting position probabilities
    grid = 3
    race_estimate_given_grid = pehd.compute_conditioning_on_grid_race_estimate(
        grid=grid,
        driver_championship_standing=driver_championship_standing,
        constructor_championship_standing=constructor_championship_standing,
        ci=ci
    )

    print(f"Prob of winning race (starting from {grid}): {race_estimate_given_grid.ci_position_probabilities.loc[1].to_dict()}")
    print(f"Prob finishing race in top 3 (starting from {grid}): {race_estimate_given_grid.ci_position_probabilities.loc[3].to_dict()}")
    print(f"Prob finishing race in top 5 (starting from {grid}): {race_estimate_given_grid.ci_position_probabilities.loc[5].to_dict()}")
    print(f"Prob finishing race in top 10 (starting from {grid}): {race_estimate_given_grid.ci_position_probabilities.loc[10].to_dict()}")
