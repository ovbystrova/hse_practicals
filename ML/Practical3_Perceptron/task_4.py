from random import randint

from task_1 import Scalar, Vector
from task_2 import PerceptronTrain, PerceptronTest


if __name__ == "__main__":

    import random
    random.seed(42)

    xs = [Vector(randint(-100, 100), randint(-100, 100)) for i in range(500)]
    ys = [Scalar(1) if x.entries[0] * x.entries[1] < 0 else Scalar(-1) for x in xs]

    _split = int(0.9 * len(xs))
    X_train, X_test = xs[:_split], xs[_split:]
    y_train, y_test = ys[:_split], ys[_split:]

    D = list(zip(X_train, y_train))
    weights, bias = PerceptronTrain(D=D,
                                    MaxIter=100)

    correct_predictions = 0
    for x, y in zip(X_test, y_test):
        y_pred = PerceptronTest(weights=weights,
                                bias=bias,
                                X=x)
        if y_pred == y.sign():
            correct_predictions += 1

    print(f"{correct_predictions} of {len(y_test)} predictions are correct.")
    print(f"Accuracy score: {correct_predictions/len(y_test)}")