import numpy as np
import pandas as pd

def single_feature_score(data, goal, feature):
    pos = data[data[feature] == True][goal]
    neg = data[data[feature] == False][goal]
    total = np.sum(pos.value_counts().idxmax() == pos) + np.sum(neg.value_counts().idxmax() == neg)
    score = total / len(data)
    return score


# Use this to find the best feature:
def best_feature(data, goal, features):
  # optional: avoid the lambda using `functools.partial`
  return max(features, key=lambda f: single_feature_score(data, goal, f))

def worst_feature(data, goal, features):
  # optional: avoid the lambda using `functools.partial`
  return min(features, key=lambda f: single_feature_score(data, goal, f))


if __name__ == '__main__':
    df = pd.read_csv('data/data_after_task2.csv', encoding='utf-8')

    features = ['easy', 'ai', 'systems', 'theory', 'morning']

    print('The best Feature is :', best_feature(df, goal='ok', features=features))
    print('The worst Feature is :', worst_feature(df, goal='ok', features=features))
