import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')
    print(df.head())


calculate_demographic_data()