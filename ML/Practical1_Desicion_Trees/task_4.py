import pandas as pd

from task_3 import best_feature
from task_1 import Tree


def DecisionTreeTrain(data, goal, features):
    """
    :param data: pd.DataFrame
    :param goal: str
    :param features: List[str]
    :return:
    """
    guess = data[goal].value_counts().idxmax()
    if len(data[goal].unique()) == 1:
        return Tree.leaf(guess)
    elif len(features) == 0:
        return Tree.leaf(guess)
    else:
        # print(len(features))
        b_feature = best_feature(data, goal, features)
        yes = data[data[b_feature] == True]
        no = data[data[b_feature] == False]
        features.remove(b_feature)
        left = DecisionTreeTrain(no, 'ok', features)
        right = DecisionTreeTrain(yes, 'ok', features)
    return Tree(data=b_feature, left=left, right=right)


def DecisionTreeTest(tree, test_point):
    """

    :param tree: Tree
    :param test_point:
    :return:
    """
    if tree.is_leaf():
        return tree.data
    if test_point[tree.data] == False:
        return DecisionTreeTest(tree.left, test_point)
    else:
        return DecisionTreeTest(tree.right, test_point)


if __name__ == '__main__':

    df = pd.read_csv('data/data_after_task2.csv', encoding='utf-8')

    features = ['easy', 'ai', 'systems', 'theory', 'morning']

    tree = DecisionTreeTrain(data=df, goal='ok', features=features)
    print(tree)

