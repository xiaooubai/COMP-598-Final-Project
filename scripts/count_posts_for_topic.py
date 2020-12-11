import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def count_posts(df, topic):
    coding_list = [code for code in df['coding']]
    return coding_list.count(topic) / len(coding_list)


def main():
    conservative_file = "data/conservative_annotated/file.tsv"
    politics_file = "data/politics_annotated/file.tsv"

    topic_list = ['policy', 'economy_climate', 'lawsuit', 'covid', 'transition', 'dissatisfaction',
                  'vote', 'discrimination']

    conservative_df = pd.read_csv(conservative_file, sep="\t")
    politics_df = pd.read_csv(politics_file, sep="\t")

    topic_proportions_conservative = []
    topic_proportions_politics = []

    for topic in topic_list:
        topic_proportions_conservative.append(count_posts(conservative_df, topic))
        topic_proportions_politics.append(count_posts(politics_df, topic))

    labels = topic_list

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, topic_proportions_conservative, width, label='Conservative')
    ax.bar(x + width / 2, topic_proportions_politics, width, label='Politics')

    ax.set_ylabel('Proportion of posts')
    ax.set_xlabel('Topic')
    ax.set_title('Distribution of Topic Engagement for Each Subreddit')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
