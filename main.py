import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

def main():
    df = pd.DataFrame.from_dict(
        [
            {"a": 1, "b": 3},
            {"a": 2, "b": 3}
        ]
    )

    print(df.describe())

    sns_plot = sns.barplot(data=df)
    sns_plot.get_figure().savefig('images/sample.png')

    print("Done")


if __name__ == "__main__":
    main()