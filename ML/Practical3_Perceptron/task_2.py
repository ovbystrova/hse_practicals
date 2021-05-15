from task_1 import Scalar, Vector


def PerceptronTrain(D, MaxIter: int = 100):
    """
    Function for Perceptron training
    Args:
        D: dataset
        MaxIter: maximum number of iterations to run

    Returns: weights and bias
    """
    bias = Scalar(0)
    weights = Vector.zero(len(D[0][0]))
    for epoch in range(MaxIter):
        for X, y in D:
            activation = X * weights + bias
            if (activation * y).sign() <= 0:
                weights = weights + y * X
                bias += y
    return weights, bias


def PerceptronTest(weights: Vector, bias: Scalar, X):
    """
    Function for Perceptron testing
    Args:
        weights: Vector
        bias: Scalar
        X: items for testing

    Returns:

    """
    activation = X * weights + bias
    return activation.sign()
