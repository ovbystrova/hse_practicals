import numpy as np
from numpy.typing import ArrayLike
import matplotlib.pyplot as plt

def scatter_clusters(centers: ArrayLike,
                     spread: ArrayLike,
                     n_points: int):
    X = []
    Y = []
    for i, c in enumerate(centers):
        X.append(c[0])
        Y.append(c[1])
        _x = np.random.randint(low=c[0] - spread[i],
                               high=c[0] + spread[i],
                               size=n_points)
        _y = np.random.randint(low=c[1] - spread[i],
                               high=c[1] + spread[i],
                               size=n_points)

        X.extend(_x.tolist())
        Y.extend(_y.tolist())

    points = [[x, y] for x, y in zip(X, Y)]

    return points


if __name__ == '__main__':
    centers = [[23, 23], [0, 0], [-15, -15]]
    points_easy = scatter_clusters(centers=centers,
                                   spread=[3, 7, 5],
                                   n_points=50)
    x, y = zip(*points_easy)
    x_centers, y_centers = zip(*centers)
    plt.title("Easy example for 3 clusters")
    plt.plot(x, y, 'o', color='blue')
    plt.plot(x_centers, y_centers, 'o', color='red')
    plt.savefig('data/task1_easy.png')

    points_hard = scatter_clusters(centers=centers,
                                   spread=[10, 10, 15],
                                   n_points=50)
    x, y = zip(*points_hard)
    x_centers, y_centers = zip(*centers)
    plt.title("Hard example for 3 clusters")
    plt.plot(x, y, 'o', color='blue')
    plt.plot(x_centers, y_centers, 'o', color='red')
    plt.savefig('data/task1_hard.png')
