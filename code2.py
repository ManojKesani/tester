import unittest
import pandas as pd
import os

class TestCode1(unittest.TestCase):
    def setUp(self):
        # Run the code in code1.py to generate the output file
        exec(open("code1.py").read())

    def test_output_file_exists(self):
        self.assertTrue(os.path.exists('output.csv'))

    def test_output_file_columns(self):
        output_df = pd.read_csv('output.csv')
        self.assertEqual(list(output_df.columns), ['ID', 'Name'])

    def test_output_file_rows(self):
        input_df = pd.read_csv('input.csv')
        output_df = pd.read_csv('output.csv')
        self.assertEqual(len(input_df), len(output_df))

    def test_output_file_data(self):
        input_df = pd.read_csv('input.csv')
        output_df = pd.read_csv('output.csv')
        for index, row in input_df.iterrows():
            name = row['First_Name'] + ' ' + row['Last_Name']
            self.assertEqual(output_df.loc[index, 'Name'], name)

if __name__ == '__main__':
    unittest.main()