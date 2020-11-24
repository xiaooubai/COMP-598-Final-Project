import argparse
import re


def to_regex(word):
    multi_case = ''
    for char in word:
        multi_case += '[' + char.lower() + char.upper() + ']'

    pattern_1 = r'\W' + multi_case + r'\W'
    pattern_2 = r'^' + multi_case + r'\W'
    pattern_3 = r'\W' + multi_case + r'$'
    pattern_4 = r'^' + multi_case + r'$'
    return [re.compile(pattern_1), re.compile(pattern_2), re.compile(pattern_3), re.compile(pattern_4)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--words', type=str, required=True, nargs='+',
                        help="a list of words (all in lowercase and separated by whitespaces) by which to filter the "
                             "posts")

    args = parser.parse_args()
    words = args.words
    regex_words = [to_regex(word) for word in words]  # This is a 2D list!

    for regex_pattern in regex_words:
        for regex in regex_pattern:
            print(regex.search("dfgdf,Trump"))


if __name__ == "__main__":
    main()
