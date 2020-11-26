import argparse
import re
import json


def to_regex(word):
    multi_case = ''
    for char in word:
        multi_case += '[' + char.lower() + char.upper() + ']'

    pattern_1 = r'\W' + multi_case + r'\W'
    pattern_2 = r'^' + multi_case + r'\W'
    pattern_3 = r'\W' + multi_case + r'$'
    pattern_4 = r'^' + multi_case + r'$'
    return [re.compile(pattern_1), re.compile(pattern_2), re.compile(pattern_3), re.compile(pattern_4)]


def read_posts(file):
    posts = []
    with open(file, 'r') as f:
        for line in f:
            post = json.loads(line)
            posts.append(post)

    return posts


def filter_posts(posts, regex_words):
    filtered_posts = []
    for post in posts:
        append = False
        for word in regex_words:
            if (word[0].search(post['title']) is not None) or (word[1].search(post['title']) is not None) or \
                    (word[2].search(post['title']) is not None) or (word[3].search(post['title']) is not None):
                append = True
        if append:
            filtered_posts.append(post)

    return filtered_posts


def write_json(posts, output_file):
    with open(output_file, 'w') as f:
        for post in posts:
            line = json.dumps(post)
            f.write(line)
            f.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True,
                        help="path to json file where to filter the posts from")
    parser.add_argument('-o', '--output', type=str, required=True,
                        help="path to file where to write the filtered posts")
    parser.add_argument('-w', '--words', type=str, required=True, nargs='+',
                        help="a list of words (all in lowercase and separated by whitespaces) by which to filter the "
                             "posts")

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    words = args.words
    regex_words = [to_regex(word) for word in words]  # This is a 2D list!

    posts = read_posts(input_file)
    filtered_posts = filter_posts(posts, regex_words)

    write_json(filtered_posts, output_file)


if __name__ == "__main__":
    main()
