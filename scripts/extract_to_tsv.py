import random
import argparse
import json
import pandas as pd


def read_posts(file, indices):
    posts = []
    with open(file, 'r') as f:
        for ix, line in enumerate(f):
            if ix in indices:
                post = json.loads(line)
                posts.append(post)

    return posts


def get_line_numbers(file):
    with open(file, 'r') as f:
        for n, _ in enumerate(f):
            pass
        return n + 1


def output(posts, output_file):
    df = pd.DataFrame({"Name": [post["name"] for post in posts],
                       "title": [post["title"] for post in posts],
                       "coding": ["" for post in posts]})
    df.to_csv(output_file, sep="\t", index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True, help="Path to output tsv file.")
    parser.add_argument('posts', help="Path to JSON file from where to extract posts.")
    parser.add_argument('num_posts', type=int, help="Number of posts to extract.")
    args = parser.parse_args()

    output_file = args.output
    posts_file = args.posts
    num_posts_to_extract = args.num_posts

    num_lines = get_line_numbers(posts_file)
    if num_posts_to_extract >= num_lines:
        lines_to_read = range(num_lines)
    else:
        lines_to_read = random.sample(range(num_lines), num_posts_to_extract)

    posts = read_posts(posts_file, lines_to_read)
    output(posts, output_file)


if __name__ == "__main__":
    main()
