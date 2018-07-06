import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q01_scrape_date
from inspect import getfullargspec
import pandas

path = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170101&end=20180401"
df = q01_scrape_date(path)


class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q01_scrape_date).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_read_csv_data_to_df_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(df.shape, (456, 7), "The Expected return shape does not match with the given return shape")

    def test_values(self):
        self.assertEqual(df.iloc[3,2], 1159.42, "The Expected return value does not match with the given return value")
