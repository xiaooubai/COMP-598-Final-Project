import argparse
import json


def read_posts(file):
    posts = []
    with open(file, 'r') as f:
        for line in f:
            post = json.loads(line)
            posts.append(post)

    return posts


def write_json(posts, output_file):
    with open(output_file, 'w') as f:
        for post in posts:
            line = json.dumps(post)
            f.write(line)
            f.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', type=str, required=True, nargs='+',
                        help="a list of file paths whose posts you want to merge in this order")
    parser.add_argument('-o', '--output', type=str, required=True,
                        help="path to file where to write the merged posts")
    args = parser.parse_args()

    files_list = args.files
    output_file = args.output

    collected_posts = []

    for file in files_list:
        collected_posts.extend(read_posts(file))

    write_json(collected_posts, output_file)


if __name__ == "__main__":
    main()
