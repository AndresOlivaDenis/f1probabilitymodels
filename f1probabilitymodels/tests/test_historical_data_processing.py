import unittest
import pandas as pd

from f1probabilitymodels.historical_data_processing.historical_data_processing_m1 import process_historical_historical_data_m1
from f1probabilitymodels.historical_data_processing.tools import compute_historical_sub_data_set

TESTS_PATH = "data/"

TESTS_HISTORICAL_RACES_RESULTS_PATH = TESTS_PATH + "historical_races_results/"
TESTS_DRIVER_STANDINGS_FILE_PATH = TESTS_HISTORICAL_RACES_RESULTS_PATH + "driver_standings.csv"
TESTS_RESULTS_FILE_PATH = TESTS_HISTORICAL_RACES_RESULTS_PATH + "results.csv"
TESTS_RACES_FILE_PATH = TESTS_HISTORICAL_RACES_RESULTS_PATH + "races.csv"
TESTS_QUALIFYING_FILE_PATH = TESTS_HISTORICAL_RACES_RESULTS_PATH + "qualifying.csv"
TESTS_DRIVERS_FILE_PATH = TESTS_HISTORICAL_RACES_RESULTS_PATH + "drivers.csv"
TESTS_CONSTRUCTOR_FILE_PATH = TESTS_HISTORICAL_RACES_RESULTS_PATH + "constructor_standings.csv"


class TestHistoricalDataProcessing(unittest.TestCase):

    df_data, df_data_all = process_historical_historical_data_m1(
        driver_standings_file_path=TESTS_DRIVER_STANDINGS_FILE_PATH,
        results_file_path=TESTS_RESULTS_FILE_PATH,
        races_file_path=TESTS_RACES_FILE_PATH,
        qualifying_file_path=TESTS_QUALIFYING_FILE_PATH,
        drivers_file_path=TESTS_DRIVERS_FILE_PATH,
        constructor_file_path=TESTS_CONSTRUCTOR_FILE_PATH
    )

    def test_process_historical_historical_data_m1(self):
        exoected_results_file = TESTS_PATH + "expected_results/process_historical_historical_data_m1.csv"
        expected_df = pd.read_csv(exoected_results_file)

        pd.testing.assert_frame_equal(expected_df, self.df_data.copy())
        # df_data.to_csv(exoected_results_file, index=False)

    def test_tools_compute_historical_sub_data_set(self):

        # sub_data_set_one
        exoected_results_file = TESTS_PATH + "expected_results/sub_data_set_one.csv"
        expected_data_set_one_df = pd.read_csv(exoected_results_file)

        df_sub_data_set_one = compute_historical_sub_data_set(self.df_data.copy(),
                                                              grid=[2, 3],
                                                              driver_championship_standing=[5, 6],
                                                              year_lower_threshold=2008,
                                                              round_lower_threshold=5)
        df_sub_data_set_one = df_sub_data_set_one.drop(columns=['constructor_standing_position'])
        df_sub_data_set_one = df_sub_data_set_one.reset_index(drop=True)

        pd.testing.assert_frame_equal(df_sub_data_set_one, expected_data_set_one_df)

        # sub_data_set_two
        exoected_results_file = TESTS_PATH + "expected_results/sub_data_set_two.csv"
        expected_data_set_two_df = pd.read_csv(exoected_results_file)

        df_sub_data_set_two = compute_historical_sub_data_set(self.df_data.copy(),
                                                              grid=3,
                                                              driver_championship_standing=5,
                                                              year_lower_threshold=2008,
                                                              round_lower_threshold=5)
        df_sub_data_set_two = df_sub_data_set_two.drop(columns=['constructor_standing_position'])
        df_sub_data_set_two = df_sub_data_set_two.reset_index(drop=True)

        pd.testing.assert_frame_equal(df_sub_data_set_two, expected_data_set_two_df)

        # sub_data_set_three
        exoected_results_file = TESTS_PATH + "expected_results/sub_data_set_three.csv"
        expected_data_set_three_df = pd.read_csv(exoected_results_file)

        df_sub_data_set_three = compute_historical_sub_data_set(self.df_data.copy(),
                                                                grid=None,
                                                                driver_championship_standing=[2, 3],
                                                                year_lower_threshold=None,
                                                                round_lower_threshold=5)
        df_sub_data_set_three = df_sub_data_set_three.drop(columns=['constructor_standing_position'])
        df_sub_data_set_three = df_sub_data_set_three.reset_index(drop=True)

        pd.testing.assert_frame_equal(df_sub_data_set_three, expected_data_set_three_df)

    def test_tools_compute_historical_sub_data_set_constructor_tandings(self):

        # sub_data_set_one
        exoected_results_file = TESTS_PATH + "expected_results/sub_data_set_one_constructor.csv"
        expected_data_set_one_df = pd.read_csv(exoected_results_file)

        df_sub_data_set_one = compute_historical_sub_data_set(self.df_data.copy(),
                                                              grid=None,
                                                              driver_championship_standing=None,
                                                              constructor_championship_standing=[1, 2],
                                                              year_lower_threshold=2008,
                                                              round_lower_threshold=5)

        # df_sub_data_set_one.to_csv(exoected_results_file, index=False)
        df_sub_data_set_one = df_sub_data_set_one.reset_index(drop=True)

        pd.testing.assert_frame_equal(df_sub_data_set_one, expected_data_set_one_df)

        # sub_data_set_two
        exoected_results_file = TESTS_PATH + "expected_results/sub_data_set_two_constructor.csv"
        expected_data_set_two_df = pd.read_csv(exoected_results_file)

        df_sub_data_set_two = compute_historical_sub_data_set(self.df_data.copy(),
                                                              grid=1,
                                                              driver_championship_standing=None,
                                                              constructor_championship_standing=[3, 4],
                                                              year_lower_threshold=2008,
                                                              round_lower_threshold=5)

        # df_sub_data_set_two.to_csv(exoected_results_file, index=False)
        df_sub_data_set_two = df_sub_data_set_two.reset_index(drop=True)

        pd.testing.assert_frame_equal(df_sub_data_set_two, expected_data_set_two_df)

        # sub_data_set_three
        exoected_results_file = TESTS_PATH + "expected_results/sub_data_set_three_constructor.csv"
        expected_data_set_three_df = pd.read_csv(exoected_results_file)

        df_sub_data_set_three = compute_historical_sub_data_set(self.df_data.copy(),
                                                                grid=[1, 2, 3],
                                                                driver_championship_standing=2,
                                                                constructor_championship_standing=[3, 4],
                                                                year_lower_threshold=2008,
                                                                round_lower_threshold=5)

        # df_sub_data_set_three.to_csv(exoected_results_file, index=False)
        df_sub_data_set_three = df_sub_data_set_three.reset_index(drop=True)

        pd.testing.assert_frame_equal(df_sub_data_set_three, expected_data_set_three_df)
