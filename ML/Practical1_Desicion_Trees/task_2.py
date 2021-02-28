import pandas as pd


if __name__ == '__main__':

    df = pd.read_csv('data/data.csv', encoding='utf-8')
    df['ok'] = df.rating.apply(lambda x: True if x >= 0 else False)
    df.to_csv('data/data_after_task2.csv', index=False)
