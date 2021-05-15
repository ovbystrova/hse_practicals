# Task 1

Implement your own Scalar and Vector classes, without using any other modules:

Both classes are implemented in `task_1.py`

# Task 2

Implement the PerceptronTrain and PerceptronTest functions, using your Vector and Scalar classes. Do not permute the dataset when training; run through it linearly.
(Hint on how to use the classes: make w and x instances of Vector, y and b instances of Scalar. What should the type of D be? Where do you see the vector operation formulas?)

Both functions are implemented in `task_2.py`

# Task 3

Make a 90-10 test-train split and evaluate your algorithm on the following dataset:

Run the following command:
```sh
python task_3.py
```

You should get these results:
```
40 of 50 predictions are correct.
Accuracy score: 0.8
```

# Task 4

Make a 90-10 test-train split and evaluate your algorithm on the xor dataset:

Run the following command:
```sh
python task_4.py
```

You should get these results:
```
26 of 50 predictions are correct.
Accuracy score: 0.52
```