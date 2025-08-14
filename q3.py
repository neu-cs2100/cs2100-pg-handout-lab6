import pandas as pd

"""
This Lab uses a dataset stored in spam.csv (in the current directory).
The original dataset is available at https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

Implement this class to use Pandas to read the data into a dataframe.
"""

class SpamReader:
    def __init__(self):
        # Read spam.csv into a dataframe, stored as a private attribute (two underscores)
        pass

    def get_dictionary(self) -> set[str]:
        # Return a set of all words that appear in the messages. You may split using whitespace
        # (ignoring the issues with punctuation).
        pass

    def word_frequency_correlation(self) -> float:
        # For each word in the dictionary (from get_dictionary()), count the number of times
        # that it appears in spam, and the number of times that it appears in ham.
        # Return the correlation between spam frequencies and ham frequencies.
        pass

    def plot_word_frequencies(self) -> None:
        # For each word in the dictionary (from get_dictionary()), count the number of times
        # that it appears in spam, and the number of times that it appears in ham.
        # Plot it with ham on the x axis and spam on the y axis.
        pass
