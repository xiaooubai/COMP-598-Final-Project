import argparse
import json
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


def is_word_present(sentence, regex):
    if (regex[0].search(sentence) is not None) or (regex[1].search(sentence) is not None) or \
            (regex[2].search(sentence) is not None) or (regex[3].search(sentence) is not None):
        return True

    return False


def get_num_posts(file, regex_president, regex_trump, regex_biden):
    num_posts_with_only_president_elect = 0
    lines_list = []
    i = 0
    with open(file, 'r') as f:
        for line in f:
            i += 1
            post = json.loads(line)
            title = post['title']
            if (is_word_present(title, regex_president)) and (not is_word_present(title, regex_trump)) and \
                    (not is_word_present(title, regex_biden)):
                num_posts_with_only_president_elect += 1
                lines_list.append(i)

    return num_posts_with_only_president_elect, lines_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True)
    args = parser.parse_args()
    file = args.file

    kw_p_e = "president-elect"
    kw_t = "trump"
    kw_b = "biden"
    regex_president = to_regex(kw_p_e)
    regex_trump = to_regex(kw_t)
    regex_biden = to_regex(kw_b)
    num_lines, lines_list = get_num_posts(file, regex_president, regex_trump, regex_biden)
    print(f"number of lines: {num_lines}")
    print(f"list of lines: {lines_list}")


if __name__ == "__main__":
    main()
