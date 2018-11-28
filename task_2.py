from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def main():
    lottery_df = pd.read_csv("lottery.csv")
    valid_columns = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
    input_data = np.array(lottery_df[valid_columns[:3]])
    print(input_data)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(input_data)
    print(kmeans.labels_)
    print(kmeans)


if __name__ == '__main__':
    main()
