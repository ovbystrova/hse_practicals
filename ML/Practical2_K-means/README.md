
# Task 1
Write a clustering problem generator with signature:

For k=3, generate easy and hard problems and plot them

`run python task_1.py`

All plots are saved in `data/task1_easy.png` and  `data/task1_hard.png`

# Task 2
Implement K-means clustering as shown in Daumé:

`Not Implemented`

# Task 3

Study the performance of these two implementations: memory, speed, quality; compare against scipy.cluster.vq.kmeans.

`Not Implemented`

# Task 4

Compute the performance of your algorithm as percent of points assigned the correct cluster. (Your algorithm may order the clusters differently!) Graph this as a function of iterations, at 10% intervals.
Make a random 10-90 test-train split; now you train on 90% of the data, and evaluate on the other 10%. How does the performance graph change?

`Not Implemented`
# Task 5

Instead of a pure 10-90 split, divide your data into 10 portions. Picking one of these portions as test and the rest as train, we have 10 different 10-90 test-train splits. Each split gives a different train-eval run, and thus a different performance number.

Perform cross-validation on your training data: plot the mean of these performances against percent-of-iterations. Error bars for these means are computed using standard deviation. Use filled plotting to show this region on the graph with matplotlib.pyplot.fill_between.

`Not Implemented`