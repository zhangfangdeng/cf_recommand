# Origin resource from MovieLens: http://grouplens.org/datasets/movielens/1m
import pandas as pd

class Channel:
    """
    simple processing for *.dat to *.csv
    """
    def __init__(self):
        self.origin_path = 'data/{}'

    def process(self):
        print('Process rating data...')
        self._process_rating_data()
        print('End.')

    def _process_rating_data(self, file='ratings.dat'):
        f = pd.read_table(self.origin_path.format(file), sep='::', engine='python',
                          names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
        f.to_csv(self.origin_path.format('ratings.csv'), index=False)


if __name__ == '__main__':
    Channel().process()