# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''
Author: Suhana Bedi
Date: 07/09/2022
Name: chembl29_test.py
Description: runs unit tests for format_chembl29.py
Run: python3 chembl29_test.py
'''
import unittest
from pandas.testing import assert_frame_equal 
from format_chembl29 import *

class TestParseMesh(unittest.TestCase): 
    """Test the functions in format_chembl29"""

    def test_main(self):
        """Test in the main function"""
        # Read in the expected output files into pandas dataframes
        df_expected = pd.read_csv('test-data/chembl_29_expected.csv')
        df_actual = pd.read_csv('test-data/chembl_29_test_data.txt', sep = '\t')
        # Run all the functions in format_chembl_uniprot.py 
        df_actual = format_col(df_actual)
        # Compare expected and actual output files
        assert_frame_equal(df_expected.reset_index(drop=True), df_actual.reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()