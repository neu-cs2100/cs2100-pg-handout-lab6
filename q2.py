import pandas as pd

# This Lab uses a dataset stored in spam.csv.
# The original dataset is available at https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

# Use Pandas to read the data into a dataframe.

class SpamReader:
    def __init__(self):
        # Read spam.csv into a dataframe, stored as a private attribute (two underscores)
        pass

    def sort_by_word_frequency(self, word: str, include_spam = True, include_ham = True) -> pd.DataFrame:
        # Return a copy of the dataframe, sorted by the frequency of times that the given
        # word appears in the message. The messages in which the word appears most often
        # should be at the top of the dataframe.
        # If include_spam is False, filter out all of the spam in the resulting dataframe.
        # If include_ham is False, filter out all of the ham in the resulting dataframe.
        pass