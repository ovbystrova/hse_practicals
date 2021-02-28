import numpy as np
from numpy.typing import ArrayLike
import matplotlib.pyplot as plt
from typing import Optional

from task_1 import scatter_clusters

def kmeans_cluster_assignment(k: int,
                              points: ArrayLike,
                              centers_guess: Optional[ArrayLike] = None,
                              max_iterations: Optional[int] = None,
                              tolerance: Optional[float] = None) -> ArrayLike:

    raise NotImplemented


if __name__ == '__main__':

    centers = [[23, 23], [0, 0], [-15, -15]]
    points_easy = scatter_clusters(centers=centers,
                                   spread=[3, 7, 5],
                                   n_points=50)
    x_easy, y_easy = zip(*points_easy)
    x_centers_easy, y_centers_easy = zip(*centers)
