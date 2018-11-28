from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

import numpy as np
import pandas as pd

def main():
    lottery_df = pd.read_csv("lottery.csv")
    valid_columns = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
    input_data = np.array(lottery_df[valid_columns[:3]])
    kmeans = KMeans(n_clusters=3, random_state=0).fit(input_data)
    fig = plt.figure(1, figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    labels = kmeans.labels_
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.scatter(input_data[:,0], input_data[:,1], input_data[:,2],
        c=labels.astype(np.float), edgecolor='k')
    fig.show()
    plt.show()
    print(kmeans)


if __name__ == '__main__':
    main()
